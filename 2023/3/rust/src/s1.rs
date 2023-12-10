use std::collections::HashMap;

use rust_helper::input_file;


struct Number{
    num:i32,
    x:i32,
    y:i32,
    len:i32,
    has_connection:bool
}


pub fn run(  )
{
    println!("p1!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!());

    let array_w = input_text.get(0).unwrap().trim().len();
    let array_h = input_text.len();
    println!("w: {}, h: {}",array_w,array_h);

    //let mut grid : Vec<Vec<char>> = vec![vec![0; 1000]; 1000] ;
    let mut num_list :HashMap<String,Number> = HashMap::new();
    let mut symbol_list : HashMap<String,String> = HashMap::new();

    let mut in_number = false;
    let mut tmp_num = String::from("");
    
    for kv_line in input_text.iter().enumerate()
    {
        //edge case for numbers at the end of a line ~
        if in_number
        {
            println!("FOUND END OF LINE NUMBER");
            let num_len: i32 = tmp_num.len() as i32; 
            in_number = false;
            let parsed_num = Number{
                num :tmp_num.parse().unwrap(),
                x :array_w as i32 - num_len,
                y :kv_line.0 as i32 - 1,
                len : tmp_num.len() as i32,
                has_connection : false
            };
            println!("iFull num: {}",parsed_num.num);
            println!(" Num x:    {}",parsed_num.x);
            println!(" Num y:    {}",parsed_num.y);
            println!(" Num len:  {}",parsed_num.len);
            num_list.insert( format!("{}:{}",kv_line.0,  parsed_num.x ), parsed_num   );
            tmp_num = String::from("");
            println!("---------");
        }
        
        for kv_letter in kv_line.1.chars().enumerate()
        {
           //println!(" {} ",kv_letter.1);
           if kv_letter.1.is_ascii_digit()
           {
               in_number = true;
               // println!("num {} ",kv_letter.1);
               tmp_num.push(kv_letter.1);
               continue;
           }
           else if in_number 
           {
               let num_len: i32 = tmp_num.len() as i32; 
               in_number = false;
               let parsed_num = Number{
                   num :tmp_num.parse().unwrap(),
                   x :kv_letter.0 as i32 - num_len,
                   y :kv_line.0 as i32,
                   len : tmp_num.len() as i32,
                   has_connection : false
               };
               // println!("iFull num: {}",parsed_num.num);
               // println!(" Num x:    {}",parsed_num.x);
               // println!(" Num len:  {}",parsed_num.len);
               num_list.insert( format!("{}:{}",kv_line.0,  parsed_num.x ), parsed_num   );
               tmp_num = String::from("");
           }

           if kv_letter.1 != '.'
           {
               symbol_list.insert( format!("{}:{}",kv_line.0,kv_letter.0), kv_letter.1.to_string());
           }
        }
    }

    //edge case for numbers at the end of the whole list ~
    if in_number
    {
        println!("FOUND END OF GRUD NUMBER");
        let num_len: i32 = tmp_num.len() as i32; 
        in_number = false;
        let parsed_num = Number{
            num :tmp_num.parse().unwrap(),
            x :array_w as i32 - num_len,
            y :array_h as i32 - 1,
            len : tmp_num.len() as i32,
            has_connection : false
        };
        println!("iFull num: {}",parsed_num.num);
        println!(" Num x:    {}",parsed_num.x);
        println!(" Num y:    {}",parsed_num.y);
        println!(" Num len:  {}",parsed_num.len);
        num_list.insert( format!("{}:{}",parsed_num.y,  parsed_num.x ), parsed_num   );
        tmp_num = String::from("");
        println!("---------");
    }
    


    println!(" l num : {}\n l sym: {}", num_list.len(),symbol_list.len());
    let mut sum = 0;
    for num_tup in num_list
    {
        //println!("checking num: {}", num_tup.1.num);
        //println!(" x:{}\n y:{} \n len:{}",num_tup.1.x, num_tup.1.y, num_tup.1.len);
        let start_x = num_tup.1.x;
        let end_x = num_tup.1.x + num_tup.1.len;
        let num_y = num_tup.1.y;
        
        'y_loop: for y in num_y-1..=num_y+1
        {
            for x in start_x-1..=end_x
            {
                let idx = format!("{}:{}", y, x);

                //println!(" idx {}",idx);
                if symbol_list.contains_key(&idx)
                {
                    // println!("  found symbol");
                    sum+= num_tup.1.num;
                    break 'y_loop;
                }
            }
        }
    }

    println!("Sum: {}",sum);

}

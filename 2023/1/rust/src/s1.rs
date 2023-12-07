use rust_helper::input_file;

pub fn run(  )
{
    println!("p1!!");
    let mut sum = 0;
    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!(true));

    
    for line in input_text
    {
        let mut num_list: Vec<char> = Vec::new();
        for letter in line.chars()
        {
            if letter.is_ascii_digit()
            {
                // println!("{}",letter);
                num_list.push(letter);
            }
        }
        
        let mut num_part: String= String::from("");
        num_part.push(num_list[0]);
        num_part.push(num_list[num_list.len()-1]);

        let num : i32 = num_part.parse().unwrap();
        println!("rnum {}",num);
        sum+= num;
    }
    println!("SUM: {}",sum);
}

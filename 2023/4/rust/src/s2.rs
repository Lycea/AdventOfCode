use rust_helper::input_file;
use std::collections::HashMap;

fn filter_empty(string_list: Vec<String>) -> Vec<String>
{
    let mut new_list : Vec<String> = vec!();

    for item in string_list
    {
        if item.is_empty() == false
        {
            //println!("Pushing item: {item}");
            new_list.push(item);
        }
    }
    return new_list;
}

pub fn run(  )
{
    println!("p2!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!());

    let card_split = rust_helper::split_array_by(&input_text
                                , ":");

    let mut card_sum = 0;
    println!("{} :: {}", card_split[0][0], card_split[0][1] );

    let mut num_map: HashMap<i32,i32>  = HashMap::new() ;

    let mut id=0;

    for card in card_split
    {
        if num_map.contains_key(&id) == false
        {            
            num_map.insert(id,0);
        }
        *num_map.get_mut(&id).unwrap()+=1;

        println!("  Actual processing sum {}", num_map.get(&id).unwrap());
        println!("  Card id: {}",id);

        let list_split = rust_helper::split_line_by(&card[1], "|");
        let winners = rust_helper::int_list( filter_empty( rust_helper::split_line_by(&list_split[0].trim().to_string(), " ") ));
        let numbers = rust_helper::int_list( filter_empty( rust_helper::split_line_by(&list_split[1].trim().to_string(), " ") ));
        let mut card_num = 0;

        println!("------------");
        for number in numbers
        {
            if winners.contains(&number)
            {

                card_num+=1;
                if num_map.contains_key( &(id + card_num)) == false
                {
                    println!("  inserting for num: {}",id+card_num);
                    num_map.insert(id + card_num,0 );
                }

                println!("  found a match");
                *num_map.get_mut(&(id + card_num)).unwrap()+=1* num_map.get(&id).unwrap();
           }
       }
       println!("CARD num: {}",card_num);

       card_sum+= num_map.get(&id).unwrap() ;
       id+=1;
    }

    println!("Endsum points: {}", card_sum);
}

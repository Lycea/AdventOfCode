use rust_helper::input_file;


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
    println!("p1!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!(false));

    let card_split = rust_helper::split_array_by(&input_text
                                , ":");

    let mut card_sum = 0;
    // println!("{} :: {}", card_split[0][0], card_split[0][1] );
    for card in card_split
    {
       let list_split = rust_helper::split_line_by(&card[1], "|");
       let winners = rust_helper::int_list( filter_empty( rust_helper::split_line_by(&list_split[0].trim().to_string(), " ") ));
       let numbers = rust_helper::int_list( filter_empty( rust_helper::split_line_by(&list_split[1].trim().to_string(), " ") ));
       let mut card_pow = 0;

       //println!("------------");
       for number in numbers
       {
           if winners.contains(&number)
           {
               card_pow+=1;
           }
       }
       //println!("CARD POW: {}",card_pow);
       let mut points = 0;
       if card_pow != 0
       {
           points = (2 as i32 ).pow(card_pow - 1);
           println!("Points: {}", (2 as i32 ).pow(card_pow - 1));
       }
       card_sum+=points;
     
    }
    println!("Endsum points: {}", card_sum);
}

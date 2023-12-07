use std::{hash::Hash, collections::HashMap};

use rust_helper::input_file;

pub fn run(  )
{
    println!("p2!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!());

    let split_games_id  = rust_helper::split_array_by(&input_text,":");
    
    let mut valid_sum = 0;

    for game in split_games_id
    {
        println!("GAME: {} ",game[0]);
        let id : i32 = rust_helper::split_line_by(&game[0]," ")[1].parse().unwrap();
        println!("  ID: {}",id);
        //split into sets
        let rounds =  rust_helper::split_array_by( &rust_helper::split_line_by(&game[1], ";" ), ",");

        let mut min_nums : HashMap<String, i32>=HashMap::from( [ (String::from("red"),0),
                                                                 (String::from("green"),0),
                                                                 (String::from("blue"),0)] );

        for round in rounds
        {
            //println!("  round:");
            for mut color in round
            {
                //println!("   Color   {}",color);
                color = color.trim().to_string();

                let col_split = rust_helper::split_line_by(&color, " ");
                //println!("   {}",col_split[0].trim());
                let num :i32 = col_split[0].trim().parse().unwrap();
                if num  > *min_nums.get(&col_split[1]).unwrap()
                {
                    min_nums.insert(col_split[1].to_string() , num);
                }
            }
        }
        println!("  Round mins: {} {} {}",min_nums["red"],min_nums["green"],min_nums["blue"]);
        let round_sum = min_nums["red"]* min_nums["blue"]* min_nums["green"];
        println!("  Sum {}",round_sum);
        valid_sum+=round_sum;
    }

    println!("\nVALID GAMES SUM: {}",valid_sum);
}

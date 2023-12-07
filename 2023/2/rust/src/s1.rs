use std::{hash::Hash, collections::HashMap};

use rust_helper::input_file;

pub fn run(  )
{
    println!("p1!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!());

    let split_games_id  = rust_helper::split_array_by(&input_text,":");
    
    let max_red = 12;
    let max_green = 13;
    let max_blue = 14;

    let mut valid_games :Vec<i32>  =  vec![] ;
    let mut valid_sum = 0;
    let mut col_alias : HashMap<String,i32>= HashMap::new();
    col_alias.insert("green".to_string(),max_green);
    col_alias.insert("red".to_string(),max_red);
    col_alias.insert("blue".to_string(),max_blue);

    for game in split_games_id
    {
        println!("GAME: {} ",game[0]);
        let id : i32 = rust_helper::split_line_by(&game[0]," ")[1].parse().unwrap();
        println!("  ID: {}",id);
        //split into sets
        let rounds =  rust_helper::split_array_by( &rust_helper::split_line_by(&game[1], ";" ), ",");

        let mut round_doable = true;

        'br_round: for round in rounds
        {
            //println!("  round:");
            for mut color in round
            {
                //println!("   Color   {}",color);
                color = color.trim().to_string();

                let col_split = rust_helper::split_line_by(&color, " ");
                //println!("   {}",col_split[0].trim());
                let num :i32 = col_split[0].trim().parse().unwrap();
                if num  > *col_alias.get(&col_split[1]).unwrap()
                {
                    println!(" invalid game!");
                    println!(" {} {} > {}",color, num, *col_alias.get(&col_split[1]).unwrap() );
                    round_doable = false;
                    break 'br_round; 
                }
                
            }

        }

        if round_doable == true
        {
            valid_sum+=id;
        }
    }

    println!("\nVALID GAMES SUM: {}",valid_sum);
}

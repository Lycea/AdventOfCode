use std::collections::HashMap;
use rust_helper::input_file;

pub fn run(  )
{
    println!("p1!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!());

    let mut twice_count = 0;
    let mut trice_count = 0;

    for line in input_text.iter()
    {
        let mut var_count:HashMap<char,i32> = HashMap::new() ;
        println!("{}",line);
        for letter in line.chars()
        {
            if var_count.contains_key(&letter) == true
            {
                println!("  Multi: {letter}");
                var_count.insert(letter,var_count[&letter] + 1);
            }
            else
            {
                var_count.insert(letter, 1);
            }
        }

        let mut two_found = false;
        let mut three_found = false;

        for (letter,count) in var_count.iter()
        {
            if *count == 2 && ! two_found
            {
                println!("  TWO {letter}");
                twice_count+=1;
                two_found = true;
            }
            else if *count == 3  &&  ! three_found 
            {
                println!("  THREE {letter}");
                trice_count+=1;
                three_found = true
            }
        }
    }

    println!("Twice: {twice_count}");
    println!("Trice: {trice_count}");
    let sum =twice_count *trice_count;
    println!("{sum}");
}

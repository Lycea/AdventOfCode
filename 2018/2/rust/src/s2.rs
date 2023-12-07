use rust_helper::input_file;
use std::collections::{vec_deque, VecDeque};

pub fn run(  )
{
    println!("\n\n--------");
    println!("p2!!(is still p1)");
    let input_text = rust_helper::read_lines(&input_file!());

    let mut comp_list =  VecDeque::from(input_text.clone());

    'outer: for line in input_text.iter()
    {

        comp_list.pop_front();
        for comp_line in comp_list.iter()
        {
            let mut same_chars : Vec<char> = Vec::new();
            let mut differences = 0;
            let mut comp_chars = comp_line.chars();
            let mut cnt = 0;
            for letter in line.chars()
            {
                if letter != comp_chars.nth(0).unwrap()
                {
                    differences+=1;
                    println!("  diff at pos {cnt}, letter {letter}");
                }
                else
                {
                    same_chars.push(letter);
                }
                cnt+=1;
            }
            if differences == 1
            {
                println!("Found similar lines !!! ");
                println!("   {line}");
                println!("   {comp_line}");
                //TODO: Print the list of same chars !
                break 'outer
            }
        }
    }

}

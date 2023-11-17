
use rust_helper;


pub fn run(  )
{
    let txt_lines = rust_helper::read_lines("src/input.txt");
    let numbers = rust_helper::int_list(txt_lines);

    let mut value = 0;

    for num in numbers.iter()
    {
            value+= num;
    }
    println!("End val {}", value);

}

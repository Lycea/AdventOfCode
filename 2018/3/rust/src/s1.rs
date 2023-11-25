use rust_helper::input_file;
use std::cmp;


fn split_line_by(string: &String, token: &str) -> Vec<String>
{
    let words : Vec<String> = string.split(token).map(|w| w.to_string()).collect();
    return words;
}

fn split_array_by(strings: &Vec<String>, token: &str) -> Vec<Vec<String>> {
    let mut result = Vec::new();

    for s in strings
    {
        //let words: Vec<String> = s.split(token).map(|w| w.to_string()).collect();
        let words = split_line_by(&s, token); 
        result.push(words);
    }

    return result;
}



mod rectangle{
    #[derive(Debug)] //makes a struct printable via {:?}
    pub struct Rectangle {
        pub x: i32,
        pub y: i32,
        pub w: i32,
        pub h: i32,
    }

    pub fn new(x: i32,y: i32,w: i32,h: i32) -> Rectangle
    {
        return Rectangle{x,y,w,h};   
    }

    pub fn get_overlap(r1 : &Rectangle,r2 : &Rectangle) -> (bool ,Rectangle)
    {
            let mut res : (bool,Rectangle) =(false,new(0,0,0,0));

            if r2.x < r1.x +r1.w &&
               r1.x < r2.x +r2.w &&
               r2.y < r1.y +r1.h &&
               r1.y < r2.y +r2.h
            {
                println!("collision!   \n  R1:  {:?},\n  R2:  {:?}",r1,r2  );
                let end_x = std::cmp::min(r2.x+ r2.w, r1.x+r1.w);  //width collision
                let end_y = std::cmp::min(r2.y+ r2.h, r1.y+r1.h);  //width collision

                let col_x = std::cmp::max(r2.x,r1.x);
                let col_y = std::cmp::max(r2.y,r1.y);

                //println!("  start:  {col_x} {col_y}");
                //println!("  end:    {end_x} {end_y}");
                //println!("  size:   {} {}",end_x-col_x,end_y-col_y);

                res.0= true;
                res.1= new(col_x, col_y,end_x-col_x,end_y-col_y );
                println!("  {:?}",res.1);
                // println!("  {:?}",coll_rect);
            }
            return res;
    }
}


pub fn run(  )
{

    println!("p1!!");

    let input_text = rust_helper::read_lines(
        &rust_helper::input_file!(false));

    let splitted_lines = split_array_by(&input_text, " ");

    let mut rectangles : Vec<rectangle::Rectangle> = Vec::new(); 
    let mut grid : Vec<Vec<i32>> = vec![vec![0; 1000]; 1000] ;
    let mut overlap_count = 0;

    for rect_line in splitted_lines
    {
        println!("{:?}",rect_line);
        let mut base_split = split_line_by( rect_line.get(2).unwrap(),",");
        base_split[1]= split_line_by( base_split.get(1).unwrap(),":").join("");
        
        println!("{:?}",base_split);
        let pos =  rust_helper::int_list(base_split);

        println!("{:?}",pos);
        let size = rust_helper::int_list(split_line_by( rect_line.get(3).unwrap(),"x") ); //w,h format

        let rect = rectangle::new( *pos.get(0).unwrap(),*pos.get(1).unwrap(),*size.get(0).unwrap(),*size.get(1).unwrap() );
        println!("New rect {:?}",rect);

        //compare all previous rectangles and check for collisions

        for other_rect in rectangles.iter()
        {
            let overlap = rectangle::get_overlap(&rect, other_rect);
            if overlap.0 == true
            {
                //check all grid positions of rectangle
                for y in 0..overlap.1.h
                {
                    for x in 0..overlap.1.w
                    {
                        let full_x = x +overlap.1.x;
                        let full_y = y +overlap.1.y;
                        if *grid.get(  ( full_y as usize) ).unwrap().get(( full_x as usize)).unwrap()== 0
                        {
                            grid[full_y as usize ][full_x as usize]= 1;
                            overlap_count +=1;
                        }
                        else
                        {
                            //println!("no new overlap :(");;
                        }
                    }
                }
            }
        }

        rectangles.push(rect);
    }

    println!("Overlapping fields: {overlap_count}");
}
//crust of rust

// effective rust

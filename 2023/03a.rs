// løst

use std::fs;
use std::io;
use std::collections::HashSet;
use std::collections::HashMap;

fn main() -> io::Result<()> {
    let input : String = fs::read_to_string("03.txt")?;
    
    let mut alle_tall: HashMap<(i32, i32), i32> = HashMap::new();
    let mut map: HashMap<(i32, i32), (i32, i32)> = HashMap::new();
    
    let mut gears: HashSet<(i32, i32)> = HashSet::new();
    let ikkegear = ['.', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    let siffer = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];
    

    input
        .lines()
        .enumerate()
        .for_each(|(radnr, rad)| rad
            .chars()
            .enumerate()
            .filter(|(_,s)| !ikkegear.contains(s))
            .for_each(|(kolnr, s)| {gears.insert((radnr as i32, kolnr as i32));})
        );

    let mut deltall = HashSet::new();

    let kolonner : usize = input
        .lines()
        .next()
        .unwrap()
        .chars()
        .count();

    let retninger = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1),
    ];

    input
        .lines()
        .enumerate()
        .for_each(|(radnr, s)| (0..kolonner)
            .for_each(|start| ((start+1)..(kolonner+1)) 
                .map(|slutt|
                    (
                        slutt, 
                        s.chars()
                            .skip(start)
                            .take(slutt-start)
                            .collect::<String>()
                    )
                )
                .filter(|(_, substring)| substring.chars().all(|c| siffer.contains(&c)))
                .filter(|(slutt, _)| *slutt == kolonner || !siffer.contains(&s.chars().nth(*slutt).unwrap()))
                .filter_map(|(slutt, tall)| tall.parse::<i32>().ok().map(|num| (slutt, num)))
                .for_each(|(slutt, tall)| {
                    if !map.contains_key(&(radnr as i32, start as i32)) {
                        alle_tall.insert((radnr as i32, start as i32), tall);
                    }

                    (start..slutt)
                        .for_each(|kolnr| {
                            if !map.contains_key(&(radnr as i32, kolnr as i32)) {
                                map.insert((radnr as i32, kolnr as i32), (radnr as i32, start as i32));
                            }
                            
                            let er_deltall = retninger
                                .iter()
                                .any(|(dx, dy)| gears.contains(&(radnr as i32 + dx, kolnr as i32 + dy)));
                                
                            if er_deltall {
                                deltall.insert(map[&(radnr as i32, start as i32)]);
                            }
                            
                        })

                })
            )
        );

    let tall: i32 = deltall
        .iter()
        .map(|t| alle_tall[t])
        .sum();

    println!("{}", tall);
    // 530495

    Ok(())
}
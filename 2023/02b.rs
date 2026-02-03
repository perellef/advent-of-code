// løst

use std::fs;
use std::io;
use std::collections::HashMap;

fn hent_uttrekk(s : &str) -> &str {
    s.split(": ").nth(1).unwrap()
}

fn til_fargeantall(uttrekk : &str) -> Vec<(String, i32)> {
    uttrekk
        .split(", ")
        .map(|kuler|
            (
                kuler.split_whitespace().nth(1).unwrap().to_string(),
                kuler.split_whitespace().nth(0).unwrap().parse::<i32>().unwrap()
            )
        )
        .collect()
}

fn oppdater_nokkel(map: &mut HashMap<&str, i32>, farge: &str, antall: &i32) {
    if let Some(v) = map.get_mut(farge) {
        *v = (*v).max(*antall);
    }
}

fn minste_antall_kuler(spill : &str) -> Vec<i32> {
    let mut maksimalt = HashMap::new();
    maksimalt.insert("red", 0);
    maksimalt.insert("green", 0);
    maksimalt.insert("blue", 0);

    spill
        .split("; ")
        .for_each(|uttrekk| 
            til_fargeantall(uttrekk)
                .iter()
                .for_each(|(farge, antall)|
                    oppdater_nokkel(&mut maksimalt, farge, antall)) 
        );
    
    maksimalt
        .values()
        .copied()
        .collect::<Vec<i32>>()
}

fn main() -> io::Result<()> {
    let input : String = fs::read_to_string("02.txt")?;

    let tall : i32 = input
        .lines()
        .map(|linje| hent_uttrekk(linje))
        .map(|spill| minste_antall_kuler(spill))
        .map(|kuler| kuler.iter().product::<i32>())
        .sum();

    println!("{}", tall);
    // 59795

    Ok(())
}
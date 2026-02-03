// løst

use std::fs;
use std::io;
use std::collections::HashMap;

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

fn hent_uttrekk(s : &str) -> &str {
    s.split(": ").nth(1).unwrap()
}


fn hent_game_id(s : &str) -> i32{
    s.split(": ")
        .nth(0)
        .unwrap()
        .split("Game ")
        .nth(1)
        .unwrap()
        .parse::<i32>()
        .unwrap()
}

fn er_mulig_uttrekk(spill : &str, tillatt: &HashMap<&str, i32>) -> bool {
    spill
        .split("; ")
        .all(|uttrekk| 
            til_fargeantall(uttrekk)
                .iter()
                .all(|(farge, antall)| *antall <= tillatt[farge.as_str()])
        )
}

fn main() -> io::Result<()> {
    let input : String = fs::read_to_string("02.txt")?;

    let mut tillatt = HashMap::new();
    tillatt.insert("red", 12);
    tillatt.insert("green", 13);
    tillatt.insert("blue", 14);

    let tall : i32 = input
        .lines()
        .map(|linje| (
                hent_game_id(linje),
                hent_uttrekk(linje)
            )
        )
        .filter(|info| er_mulig_uttrekk(info.1, &tillatt))
        .map(|info| info.0)
        .sum();

    println!("{}", tall);
    // 2617

    Ok(())
}
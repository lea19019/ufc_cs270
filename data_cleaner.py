# Fight Example Data
[
    {
        "fighters": {
            "fighter1": {
                "status": "L",
                "name": "Israel Adesanya",
                "nickname": "\"The Last Stylebender\"", # Remove the inner strings, should be just a single string
                "link": "http://www.ufcstats.com/fighter-details/1338e2c7480bdf9e" # Remove the URL details and leave only the id
            },
            "fighter2": {
                "status": "W",
                "name": "Nassourdine Imavov",
                "nickname": "\"The Sniper\"",
                "link": "http://www.ufcstats.com/fighter-details/881bf86d4cba8578"
            }
        },
        "fight_details": {
            "title": "Middleweight Bout", # Extract the weight class and create a new field named 'weight_class'
            "method": "KO/TKO",
            "round": "2",
            "time": "0:30", # Convert this into a data type, we want seconds
            "time format": "5 Rnd (5-5-5-5-5)", # This means that this fight was 5 rounds each of 5 minutes, we want to express that in a diferent way and create fields for this
            "referee": "Marc Goddard",
            "details": "Punch to Head At Distance"
        },
        "totals": {
            "fighter1": {
                "KD": "0", 
                "Sig. str.": "26 of 50",
                "Sig. str. %": "52%",
                "Total str.": "32 of 56",
                "Td": "0 of 1",
                "Td %": "0%",
                "Sub. att": "0",
                "Rev.": "0",
                "Ctrl": "0:00"
            },
            "fighter2": {
                "KD": "1",
                "Sig. str.": "15 of 31",
                "Sig. str. %": "48%",
                "Total str.": "18 of 34",
                "Td": "0 of 3",
                "Td %": "0%",
                "Sub. att": "0",
                "Rev.": "0",
                "Ctrl": "0:44"
            },
            "rounds": {
                "Round 1": {
                    "fighter1": {
                        "KD": "0",
                        "Sig. str.": "20 of 44",
                        "Sig. str. %": "45%",
                        "Total str.": "26 of 50",
                        "Td %": "0%",
                        "Sub. att": "0",
                        "Rev.": "0",
                        "Ctrl": "0:00"
                    },
                    "fighter2": {
                        "KD": "0",
                        "Sig. str.": "8 of 21",
                        "Sig. str. %": "38%",
                        "Total str.": "10 of 23",
                        "Td %": "0%",
                        "Sub. att": "0",
                        "Rev.": "0",
                        "Ctrl": "0:40"
                    }
                },
                "Round 2": {
                    "fighter1": {
                        "KD": "0",
                        "Sig. str.": "6 of 6",
                        "Sig. str. %": "100%",
                        "Total str.": "6 of 6",
                        "Td %": "---",
                        "Sub. att": "0",
                        "Rev.": "0",
                        "Ctrl": "0:00"
                    },
                    "fighter2": {
                        "KD": "1",
                        "Sig. str.": "7 of 10",
                        "Sig. str. %": "70%",
                        "Total str.": "8 of 11",
                        "Td %": "---",
                        "Sub. att": "0",
                        "Rev.": "0",
                        "Ctrl": "0:04"
                    }
                }
            }
        },
        "significant_strikes": {
            "fighter1": {
                "Sig. str": "26 of 50",
                "Sig. str. %": "52%",
                "Head": "9 of 28",
                "Body": "6 of 8",
                "Leg": "11 of 14",
                "Distance": "26 of 50",
                "Clinch": "0 of 0",
                "Ground": "0 of 0"
            },
            "fighter2": {
                "Sig. str": "15 of 31",
                "Sig. str. %": "48%",
                "Head": "9 of 21",
                "Body": "0 of 3",
                "Leg": "6 of 7",
                "Distance": "10 of 25",
                "Clinch": "0 of 0",
                "Ground": "5 of 6"
            },
            "rounds": {
                "Round 1": {
                    "fighter1": {
                        "Sig. str": "20 of 44",
                        "Sig. str. %": "45%",
                        "Head": "8 of 27",
                        "Body": "3 of 5",
                        "Leg": "9 of 12",
                        "Distance": "20 of 44",
                        "Clinch": "0 of 0",
                        "Ground": "0 of 0"
                    },
                    "fighter2": {
                        "Sig. str": "8 of 21",
                        "Sig. str. %": "38%",
                        "Head": "3 of 13",
                        "Body": "0 of 2",
                        "Leg": "5 of 6",
                        "Distance": "8 of 21",
                        "Clinch": "0 of 0",
                        "Ground": "0 of 0"
                    }
                },
                "Round 2": {
                    "fighter1": {
                        "Sig. str": "6 of 6",
                        "Sig. str. %": "100%",
                        "Head": "1 of 1",
                        "Body": "3 of 3",
                        "Leg": "2 of 2",
                        "Distance": "6 of 6",
                        "Clinch": "0 of 0",
                        "Ground": "0 of 0"
                    },
                    "fighter2": {
                        "Sig. str": "7 of 10",
                        "Sig. str. %": "70%",
                        "Head": "6 of 8",
                        "Body": "0 of 1",
                        "Leg": "1 of 1",
                        "Distance": "2 of 4",
                        "Clinch": "0 of 0",
                        "Ground": "5 of 6"
                    }
                }
            }
        }
    }
]

# Fighter Example
[
    {
        "name": "Wanderlei Silva",
        "record": "Record: 35-13-1 (1 NC)",
        "nickname": "The Axe Murderer",
        "physical_attributes": {
            "Height": "5' 11\"",
            "Weight": "205 lbs.",
            "Reach": "74\"",
            "STANCE": "Orthodox",
            "DOB": "Jul 03, 1976"
        },
        "career_statistics": {
            "SLpM": "2.79",
            "Str. Acc.": "40%",
            "SApM": "2.19",
            "Str. Def": "60%",
            "TD Avg.": "0.97",
            "TD Acc.": "53%",
            "TD Def.": "62%",
            "Sub. Avg.": "0.6"
        },
        "link": "http://www.ufcstats.com/fighter-details/a1f6999fe57236e0"
    }
]

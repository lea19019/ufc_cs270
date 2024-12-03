import json

def convert_json_to_arff(json_data, output_file):
    with open(output_file, 'w') as arff:
        arff.write("@RELATION fight_outcome\n\n")
        
        # Attributes
        arff.write("@ATTRIBUTE fighter1_name STRING\n")
        arff.write("@ATTRIBUTE fighter2_name STRING\n")
        arff.write("@ATTRIBUTE fighter1_KD NUMERIC\n")
        arff.write("@ATTRIBUTE fighter2_KD NUMERIC\n")
        arff.write("@ATTRIBUTE fighter1_SigStr NUMERIC\n")
        arff.write("@ATTRIBUTE fighter2_SigStr NUMERIC\n")
        arff.write("@ATTRIBUTE fighter1_SigStrAcc NUMERIC\n")
        arff.write("@ATTRIBUTE fighter2_SigStrAcc NUMERIC\n")
        arff.write("@ATTRIBUTE fighter1_TotalStr NUMERIC\n")
        arff.write("@ATTRIBUTE fighter2_TotalStr NUMERIC\n")
        arff.write("@ATTRIBUTE fighter1_Td NUMERIC\n")
        arff.write("@ATTRIBUTE fighter2_Td NUMERIC\n")
        arff.write("@ATTRIBUTE fighter1_TdAcc NUMERIC\n")
        arff.write("@ATTRIBUTE fighter2_TdAcc NUMERIC\n")
        arff.write("@ATTRIBUTE fighter1_Ctrl STRING\n")
        arff.write("@ATTRIBUTE fighter2_Ctrl STRING\n")
        arff.write("@ATTRIBUTE method STRING\n")
        arff.write("@ATTRIBUTE round NUMERIC\n")
        arff.write("@ATTRIBUTE time STRING\n")
        arff.write("@ATTRIBUTE class {fighter1_win, fighter2_win}\n\n")
        arff.write("@DATA\n")
        
        # Data
        for fight in json_data:
            f1 = fight['fighters']['fighter1']
            f2 = fight['fighters']['fighter2']
            details = fight['fight_details']
            totals = fight['totals']
            
            f1_kd = totals['fighter1']['KD']
            f2_kd = totals['fighter2']['KD']
            f1_sigstr, f1_sigacc = map(int, totals['fighter1']['Sig. str.'].split(' of '))
            f2_sigstr, f2_sigacc = map(int, totals['fighter2']['Sig. str.'].split(' of '))
            f1_totalstr = totals['fighter1']['Total str.'].split(' of ')[0]
            f2_totalstr = totals['fighter2']['Total str.'].split(' of ')[0]
            f1_td = totals['fighter1']['Td'].split(' of ')[0]
            f2_td = totals['fighter2']['Td'].split(' of ')[0]
            f1_tdacc = totals['fighter1']['Td %'][:-1]
            f2_tdacc = totals['fighter2']['Td %'][:-1]
            f1_ctrl = totals['fighter1']['Ctrl']
            f2_ctrl = totals['fighter2']['Ctrl']
            
            winner = "fighter1_win" if f1['status'] == "W" else "fighter2_win"
            
            arff.write(f"\"{f1['name']}\",\"{f2['name']}\",{f1_kd},{f2_kd},{f1_sigstr},{f2_sigstr},"
                       f"{f1_sigacc},{f2_sigacc},{f1_totalstr},{f2_totalstr},{f1_td},{f2_td},"
                       f"{f1_tdacc},{f2_tdacc},\"{f1_ctrl}\",\"{f2_ctrl}\",\"{details['method']}\","
                       f"{details['round']},\"{details['time']}\",{winner}\n")

# Load your JSON file
with open('./important/total_fights_json.json', 'r') as file:
    data = json.load(file)

convert_json_to_arff(data, 'output.arff')

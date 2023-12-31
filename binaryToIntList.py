inputBinStr="""
"................................................................................................................................",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".########....#####.####..###..###.####......####.####..###..###.####......####.####......####.#####....#########..#############.",
".#######..##..####.####...#...###.######..######.####..###..###.######..######.####..########.####..##..########..#############.",
".#######..########.####.......###.######..######.####..###..###.######..######.####..########.####..############..#############.",
".########....#####.####..#.#..###.######..######.####..#.#..###.######..######.####....######.#####....#########..#############.",
".###########..####.####..###..###.######..######.####.......###.######..######.####..########.########..########..#############.",
".#######..##..####.####..###..###.######..######.####...#...###.######..######.####..########.####..##..########..#############.",
".########....#####.####..###..###.######..######.####..###..###.######..######.####..########.#####....#########..######.######.",
".#################.##############.##############.##############.##############.##############.##################..######..#####.",
".##..........................................................................................................###..##.....#.####.",
".#################.##############.##############.##############.##############.##############.##################..##.######.###.",
".#################.##############.##############.##############.##############.##############.##################..##.#######.##.",
".#################.##############.##############.##############.##############.##############.##################..##.######.###.",
".#################.##############.##############.##############.##############.##############.##################..##.....#.####.",
".#################.##############.##############.##############.##############.##############.##################..######..#####.",
".#################.##############.##############.##############.##############.##############.##################..######.######.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".#################.##############.##############.##############.##############.##############.##################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".#.............................................................................................................#..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..#############.",
".###############################################################################################################..######.######.",
".#.............................................................................................................#..######.######.",
".###############################################################################################################..#####.#.#####.",
".####################################################.###################################...####################..####..#..####.",
".####..........################################.####...################################.......##################..##..#####..##.",
".#####........#################################..###.#.################################.#####.##################..####..#..####.",
".###............###############################.#.#.##.################################.#####.##################..#####.#.#####.",
".##.##........##.##############################.#..###.##.#############################.#####.##################..######.######.",
".##.##........##.##############################.#####.##..#############################.#####.##################..######.######.",
".##.##........##.##############################.##.##.#.#.#############################.#####.##################..#############.",
".###............##############################.###..##..#.#############################.#####.##################..#############.",
".######......#################################.##....####.#############################.#####.##################..#############.",
".#######....##################################.##....###.##############################.#####.##################..#############.",
".########..###################################..##..####.##############################.#####.##################..#############.",
".########..####################################.#######.###############################.#####.##################..#############.",
".########..####################################..####..################################.#####.##################..#############.",
".######......###################################..##..#################################.#####.##################..#############.",
".######......####################################....##################################.......##################..#############.",
".###############################################################################################################..#############.",
"................................................................................................................................"
"""
inputBinStr=inputBinStr.replace("#","0")
inputBinStr=inputBinStr.replace(".","1")
inputBinStr=inputBinStr[::-1]
inputBinStr_clean=""
for i in inputBinStr:
  if i in ["0","1"]:
    inputBinStr_clean+=i


def bitstring_to_bytes(s):
    v = int(s, 2)
    b = bytearray()
    while v:
        b.append(v & 0xff)
        v >>= 8
    return bytes(b)
 
print(bytearray(bitstring_to_bytes(inputBinStr_clean)))

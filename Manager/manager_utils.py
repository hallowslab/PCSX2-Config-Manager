import sys

## Get user input for action to manage game
def get_manage_option(again=False):
    if not again:
        sys.stdout.write("\nSelect the actions by order if creating a new game\n \n")
    sys.stdout.write("cf : Copy files from pcsx folder to game dir\n")
    sys.stdout.write("at : Add templates to game dir, rename them, and replace values\n")
    sys.stdout.write("sm : Creates a symbolic link to shared memcards\n")
    sys.stdout.write("pg : Play game\n")
    sys.stdout.write("e : exit\n")
    action = input("\nPlease select an option(cf|at|sm|pg|e):")
    sys.stdout.write("\n")
    return action

## Return environment variables dict
def envs_to_dict(config, logger):
    env_dict = {x.lower():config["CONFIG"][x] for x in config["CONFIG"]}
    for var in env_dict:
        if env_dict[var] == "\"\"" or env_dict[var] == "" or env_dict[var] == " ":
            logger.warning("Variable empty %s" % (var))
    return env_dict

## Add arguments to parser and return them
def add_args(parser):
    ## Add group
    required_g = parser.add_argument_group("Required args")
    # required
    required_g.add_argument("-cfg", help="Configuration file", action="store", required=True)
    required_g.add_argument("-option", help="(ac|mac|m|p) ac for auto create game, mac for multiple auto creation, m for manage, p for play", action="store", required=True)
    # optional
    parser.add_argument("-debug", "--debug_level", help="Set debug level", action="store")
    parser.add_argument("--game", help="Game name, can be set in manager.ini", action="store")
    args = parser.parse_args()
    return args

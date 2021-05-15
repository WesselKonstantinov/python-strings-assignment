# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Names of the player that scored during the match
scored_player_0 = 'Ruud Gullit'
scored_player_1 = 'Marco van Basten'

# The minutes during which they scored
goal_0 = 32
goal_1 = 54

# Reports who scored and when
scorers = scored_player_0 + ' ' + \
    str(goal_0) + ', ' + scored_player_1 + ' ' + str(goal_1)
report = f'{scored_player_0} scored in the {goal_0}nd minute\n{scored_player_1} scored in the {goal_1}th minute'

print(scorers)
print(report)

# Get the first and last name of a single player
player = 'Erwin Koeman'
first_name = player[:player.find(' ')]
last_name = player[player.find(' ') + 1:]
last_name_len = len(player[player.find(' ') + 1:])
name_short = f'{first_name[0].upper()}. {last_name}'

# This is what the crowd chants when the player is about to score
chant = (f'{first_name}! ' * len(first_name))[:-1]

# Make sure the last character is not a space
good_chant = chant[-1] != ' '

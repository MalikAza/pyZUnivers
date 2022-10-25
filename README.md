![PyPI - Python Version](https://img.shields.io/pypi/pyversions/red-discordbot) ![GitHub last commit](https://img.shields.io/github/last-commit/MalikAza/Aza-Cogs)

# pyZUnivers
ZUnivers API python wrapper

## Getting started
### Installation
1. Ensure to have the following requirements : [requests](https://pypi.org/project/requests/)
2. Download the latest version of pyZUnivers.py
3. Add the file in you project and import it
### Usage
You will mainly use the `User` class which needs a discord username as argument. For more informations, see the documentation.

## Documentation
### User
The `User` is the main class of the library. It allows to get informations about a user.

#### Arguments
- `username` (*str*): The **discord username** of the user. (ex: `ZeratoR#1337`)
- `challenge` (*bool*): Boolean to have access to the challenge attribute if is `True`. *(Makes an additional API request)*
- `reputation` (*bool*): Boolean to have access to the reputation attribute if is `True`. *(Makes an additional API request)*
- `journa` (*bool*): Boolean to have access to the journa attribute if is `True`. *(Makes an additional API request)*
- `pity_andor_vortex` (*bool*): If `True` give access to => `pity_in`, `vortex_stade` & `vortex_trys` attributes. *(Makes an additional API request)*
#### Attributes
- `url` (*str*): The **url** of the user. (ex: `https://zunivers.zerator.com/joueur/ZeratoR%231337/`)
- `name` (*str*): The **name** of the user. (ex: `ZeratoR#1337`)
- `monnaie` (*int*): The amount of **ZUMonnaie** of the user.
- `powder` (*int*): The amount of **Poudrecreatrice** of the user.
- `crystal` (*int*): The amount of **Cristaldhistoire** of the user.
- `rank` (*str*): The **rank** of the user. (ex : OnlyZera)
- `active` (*bool*): The **status** of the user considered in the ZUnivers.
- `card_numbers` (*int*): The number of **cards** of the user.
- `unique_cards` (*int*): The number of **unique cards** of the user.
- `unique_gold_cards` (*int*): The number of **unique gold cards** of the user.
- `ticket_numbers` (*int*): The number of **tickets** the user has used.
- `achievement_numbers` (*int*): The number of **achievements** of the user.
- `tradeless` (*bool*): The *status* of the user if it has **traded** or not.
- `is_subscribed` (*bool*): The *status* of the user if it is **subscribed** or not.

If `is_subscribed` is `True`:
- `subscription_begin` (*datetime object*): The **beginning date** of the **subscription**.
- `subscription_end` (*datetime object*): The **end date** of the **subscription**.

If `pity_andor_vortex` is `True`:
- `pity_in` (*int*): The **number** of invocations until the **pity** strikes.
- `vortex_stade` (*int*): The current user **floor** of the **vortex**.
- `vortex_trys` (*int*): The number of **trys** the user has done in the **vortex**.

If `journa` is `True`:
- `journa` (*bool*): The **status** of the user if it has made his daily **journa** command.

If `challenge` is `True`:
- `challenge` (*Challenges Class*): See the documentation of the `Challenges` class.

If `reputation` is `True`:
- `reputation` (*_UserReputation Class*): See the documentation of the `_UserReputation` class.

- `leaderboards` (*_UserLeaderboards Class*): See the documentation of the `_UserLeaderboards` class.

___

### Challenges
The `Challenges` is the class which lists the different challenges of the user.

#### Arguments
- `username` (*Optional[str]*): The **discord username** of the user. (ex: `ZeratoR#1337`)
#### Attributes
- `first` (*_ChallengeAtrb Class*): See the different attributes of the challenges below.
- `second` (*_ChallengeAtrb Class*): See the different attributes of the challenges below.
- `third` (*_ChallengeAtrb Class*): See the different attributes of the challenges below.
- `begin_date` (*datetime object*): The **beginning date** of the weekly **challenges**.
- `end_date` (*datetime object*): The **end date** of the weekly **challenges**.

Attributes for `first`, `second` and `third`:
- `name` (*str*): The **name** of the challenge.
- `score_gain` (*int*): The **score gain** of the challenge.
- `powder_gain` (*int*): The **Poudrecreatrice gain** of the challenge.
If a `username` is provided:
- `progress` (*str*): The **progress** of the challenge. (ex: `0/10`)
- `achieved_date` (*datetime object*): The **date** when the challenge was achieved. (Returns `None` if not achieved)

___

### _UserReputation
The `_UserReputation` is the class which lists the different reputation of the user.

#### Attributes
- `first` (*_ReputationClan Class*): See the different attributes of the reputation below.
- `second` (*_ReputationClan Class*): See the different attributes of the reputation below.
- `third` (*_ReputationClan Class*): See the different attributes of the reputation below.
- `fourth` (*_ReputationClan Class*): See the different attributes of the reputation below.
- `fifth` (*_ReputationClan Class*): See the different attributes of the reputation below.

Attributes for `first`, `second`, `third`, `fourth` and `fifth`:
- `name` (*str*): The **name** of the reputation.
- `level_name` (*str*): The **level name** of the reputation.
- `progress` (*str*): The **progress** of the reputation. (ex: `0/10`)

___

### Vortex
The `Vortex` is the class of the current **Vortex**.

#### Attributes
- `name` (*str*): The **name** of the current **Vortex**.
- `pack` (*str*): The **pack name** of the current **Vortex**.
- `reputation` (*str*): The **reputation name** of the current **Vortex**.
- `begin_date` (*datetime object*): The **beginning date** of the current **Vortex**.
- `end_date` (*datetime object*): The **end date** of the current **Vortex**.

___

### Event
The `Event` is the class which lists the curent(s) **Event(s)**.

#### Attributes
- `got_events` (*bool*): Tells if there is an **Event** or not.

If `got_events` is `True`:
- `names` (*str list*): The **name(s)** of the current **Event(s)**.
- `pack_names` (*str list*): The **pack name(s)** of the current **Event(s)**.
- `monney_costs` (*int list*): The **money cost(s)** of the current **Event(s)**.
- `dust_costs` (*int list*): The **dust cost(s)** of the current **Event(s)**.
- `is_onetimes` (*bool list*): Tells if the current **Event(s)** are **one time** or not.
- `begin_dates` (*datetime list*): The **beginning date(s)** of the current **Event(s)**.
- `end_dates` (*datetime list*): The **end date(s)** of the current **Event(s)**.
- `actives` (*bool list*): Tells if the current **Event(s)** are **active** or not.

___

### Insomniaque
The `Insomniaque` is a special class for the achievement "*L'insomniaque*".

#### Arguments
- `username` (*str*): The **discord username** of the user. (ex: `ZeratoR#1337`)
#### Attributes
- `name` (*str*): The **name** of the achievement.
- `description` (*str*): The **description** of the achievement.
- `reward_score` (*int*): The **reward score** of the achievement.
- `done` (*bool*): The **status** of the achievement if it has been **achieved or not**.

If `done` is `False`:
- `progress_done` (*str list*): The **progress done** of the achievement. (ex: `0h, 1h, 12h, 13h`)
- `progress_todo` (*str list*): The **progress to do** of the achievement. (ex: `5h, 6h, 7h, 23h`)

___

### _UserLeaderboards
The `_UserLeaderboards` is the class which lists the different leaderboards of the user.

#### Attributes
- `achievement` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `challenge` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `globals` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `inventory` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `inventory_unique` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `inventory_unique_golden` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `inventory_unique_normal` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `reputation` (*_Leaderboard Class*): See the different attributes of the leaderboard below.
- `tradeless` (*_Leaderboard Class | False*): See the different attributes of the leaderboard below. ⚠️ This attribute can return `False` instead of a `_Leaderboard Class` if `User.tradeless` is `True`. ⚠️

Attributes for `achievement`, `challenge`, `globals`, `inventory`, `inventory_unique`, `inventory_unique_golden`, `inventory_unique_normal`, `reputation` & `tradeless`:
- `position` (*int*): The **position** of the user in the leaderboard.
- `score` (*int*): The **score** of the user in the leaderboard.

___

### user_journa
The `user_journa` is the method which return a **boolean** to tell if the user have done its daily `journa` command.

#### Arguments
- `username` (*str*): The **discord username** of the user. (ex: `ZeratoR#1337`)

#### Return
Return a `Boolean`. The **status** of the user if it has made his daily **journa** command.

___

### user_pity
The `user_pity` is the method which return an **int** to tell in how many **invocations** the **pity** will strikes.

#### Arguments
- `username` (*str*): The **discord username** of the user. (ex: `ZeratoR#1337`)

#### Return
Return an **int** to tell in how many **invocations** the **pity** will strikes.

___

### user_vortex_stats
The `user_vortex_stats` is the method which return the current user **floor** of the **vortex** and the number of **trys** the user has done in the **vortex**.

#### Arguments
- `username` (*str*): The **discord username** of the user. (ex: `ZeratoR#1337`)

#### Return
Return two int => The current user **floor** of the **vortex** and the number of **trys** the user has done in the **vortex**.

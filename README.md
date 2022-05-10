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
The `User` class is the main class of the library. It allows to get informations about a user.

#### Arguments
- `username`: The **discord username** of the user. (ex: `ZeratoR#1337`)
#### Attributes
- `url` (*str*): The **url** of the user. (ex: `https://zunivers.zerator.com/joueur/ZeratoR%231337/`)
- `name` (*str*): The **name** of the user. (ex: `ZeratoR#1337`)
- `position` (*int*): The **position** of the user.
- `score` (*int*): The **score** of the user.
- `score_item` (*int*): The score of the user obtained by the **cards**.
- `score_achievement` (*int*): The score of the user obtained by the **achievements**.
- `score_challenge` (*int*): The score of the user obtained by the **challenges**.
- `monnaie` (*int*): The amount of **ZUMonnaie** of the user.
- `powder` (*int*): The amount of **Poudrecreatrice** of the user.
- `crystal` (*int*): The amount of **Cristaldhistoire** of the user.
- `rank` (*str*): The **rank** of the user. (ex : OnlyZera)
- `active` (*bool*): The **status** of the user considered in the ZUnivers.
- `card_numbers` (*int*): The number of **cards** of the user.
- `unique_cards` (*int*): The number of **unique cards** of the user.
- `unique_gold_cards` (*int*): The number of **unique gold cards** of the user.
- `lucky_numbers` (*int*): The number of **tickets** the user has used.
- `achievement_numbers` (*int*): The number of **achievements** of the user.
- `tradeless` (*bool*): The *status* of the user if it has **traded** or not.
- `is_subscribed` (*bool*): The *status* of the user if it is **subscribed** or not.

If `is_subscribed` is `True`:
- `subscription_begin` (*datetime object*): The **beginning date** of the **subscription**.
- `subscription_end` (*datetime object*): The **end date** of the **subscription**.

- `pity_in` (*datetime object*): The **date** when the next **pity** will be.
- `vortex_stade` (*int*): The current user **floor** of the **vortex**.
- `vortex_trys` (*int*): The number of **trys** the user has done in the **vortex**.
- `journa` (*bool*): The **status** of the user if it has made his daily **!journa**.
- `challenge` (*Challenges Class*): See the documentation of the `Challenges` class.
- `reputation` (*_UserReputation Class*): See the documentation of the `_UserReputation` class.


### Challenges
The `Challenges` class is the class which lists the different challenges of the user.

#### Arguments
- `username` (*Optional*): The **discord username** of the user. (ex: `ZeratoR#1337`)
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


### _UserReputation
The `_UserReputation` class is the class which lists the different reputation of the user.

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


### Vortex
The `Vortex` class is the class of the current **Vortex**.

#### Attributes
- `name` (*str*): The **name** of the current **Vortex**.
- `pack` (*str*): The **pack name** of the current **Vortex**.
- `reputation` (*str*): The **reputation name** of the current **Vortex**.
- `begin_date` (*datetime object*): The **beginning date** of the current **Vortex**.
- `end_date` (*datetime object*): The **end date** of the current **Vortex**.


### Event
The `Event` class is the class which lists the curent(s) **Event(s)**.

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


### Insomniaque
The `Insomniaque` class is a special class for the achievement "*L'insomniaque*".

#### Arguments
- `username`: The **discord username** of the user. (ex: `ZeratoR#1337`)
#### Attributes
- `name` (*str*): The **name** of the achievement.
- `description` (*str*): The **description** of the achievement.
- `reward_score` (*int*): The **reward score** of the achievement.
- `done` (*bool*): The **status** of the achievement if it has been **achieved or not**.

If `done` is `False`:
- `progress_done` (*str list*): The **progress done** of the achievement. (ex: `0h, 1h, 12h, 13h`)
- `progress_todo` (*str list*): The **progress to do** of the achievement. (ex: `5h, 6h, 7h, 23h`)

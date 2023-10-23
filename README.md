# Yahoo Fantasy Football API Integration

### Overview
Download Fantasy Data From Yahoo Using the API

You can use this to build a dashboard [Here's a Tableau Example!](https://public.tableau.com/app/profile/jletienne/viz/2023CountdownFantasyFootballStats/Summary?publish=yes "dashboard")

### Instructions (Setup)

You'll need to configure oauth2yahoo.json first! This exercise is best left as an exercise for the reader.
Just kidding. I'm very funny! lol lmfao :laughing: go here https://developer.yahoo.com/apps/create/

- Name: "Yahoo Fantasy Football Integration"
- Redirect URI: https://example.com/callback
- OAuth Client Type: Confidential Client
- API Permsissions: Fantasy Sports, READ ONLY!!!!

Now your apps are here.
https://developer.yahoo.com/apps/

Click through and configure the `consumer_key` and `consumer_secret` in the oauth2yahoo.json file

### Instructions (Once A Year)

Once a year you'll need to figure out the game Id

    python get_game.py

It's in the json that's printed. Pop that mug into your config file.
- Change line 1
- Also change line 3. the First Three numbers of 414.l.XXXXX
Also in your config file upate the league ID only

### Instructions (Run this every Wednesday)
You can run this everyday if you want. But ~~definetly~~ ~~defianetly~~  ~~defintly~~ (idk spelling?) run it every Wednesday!

    python get_all_fantasy_data.py

### Done
Your data is now in prod_data go crazy!
- prod_data/fantasy_player_stats.csv
- prod_data/fantasy_team_stat.csv

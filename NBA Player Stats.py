import marimo

__generated_with = "0.17.0"
app = marimo.App(width="medium")


@app.cell
def _(mo):
    mo.md(
        r"""
    # Analysis of NBA Data from Analyst Builder
    ## Questions to Answer:

    - Which players lead their seasons in scoring, rebounding, and playmaking - and how efficient are they?
    - How do players from different eras (1990s, 2000s, 2010s, 2020s) compare in size, style, and performance?
    - Which teams, positions, or player types consistently produce top performers?
    - Based on the data, who deserves the MVP crown - and how does your pick compare to the official NBA MVP?
    """
    )
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import seaborn as sns
    return mo, pl, sns


@app.cell
def _(pl):
    nba_data = pl.read_csv('all_seasons.csv')
    nba_data
    return (nba_data,)


@app.cell
def _(mo):
    mo.md(r"""## Analysing the 90's""")
    return


@app.cell
def _(nba_data):
    players_90s = nba_data.sql("SELECT * FROM self WHERE season like '199%'")
    season_1996_97 = players_90s.sql("SELECT * FROM self WHERE season like '1996-97'")
    season_1997_98 = players_90s.sql("SELECT * FROM self WHERE season like '1997-98'")
    season_1998_99 = players_90s.sql("SELECT * FROM self WHERE season like '1998-99'")
    season_1999_00 = players_90s.sql("SELECT * FROM self WHERE season like '1999-00'")
    return


@app.cell
def _():
    #season_1996_97.sql("SELECT player_name, age, gp, pts, reb, ast  FROM self ORDER BY pts DESC")
    #season_1996_97.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY reb DESC")
    #season_1996_97.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY ast DESC")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    #### Points
    |1996-97(CHI)|1997-98(CHI)|1998-99(SAS)|1999-00(LAL)|
    |------------|------------|------------|------------|
    |Michael Jordan (29.6 pts)|Michael Jordan (28.7 pts)|Allen Iverson (26.8 pts)|Shaquille O'Neal (29.7 pts)|
    |Karl Malone (27.4 pts)|Shaquille O'Neal (28.3 pts)|Shaquille O'Neal (26.3 pts)|Allen Iverson (28.4 pts)|
    |Glen Rice (26.8 pts)|Karl Malone (27 pts)|Karl Malone (23.8 pts)|Grant Hill (25.8pts)|
    |Shaquille O'Neal (26.2 pts)|Glenn Robinson (23.4 pts)|Shareef Abdur-Rahim (23 pts)|Vince Carter (25.7 pts)|
    |Mitch Richmond (25.9 pts)|Mitch Richmond(23.2pts)|Keith Van Horn (21.8 pts)|Karl Malone (25.5 pts)|

    #### Rebounds
    |1996-97(CHI)|1997-98(CHI)|1998-99(SAS)|1999-00(LAL)|
    |------------|------------|------------|------------|
    |Dennis Rodman (16.1 reb)|Dennis Rodman (15 reb)|Chris Weber (13 reb)|Dennis Rodman (14.3 reb)|
    |Jayson Williams (13.5 reb)|Jayson Williams (13.6 reb)|Charles Barkley (12.3 reb)|Dikembe Mutombo (14.1 reb)|
    |Charles Barkley (13.5 reb)|Tim Duncan (11.9 reb)|Dikembe Mutombo (12.2 reb)|Shaquille O'Neal (13.6 reb)|
    |Shaquille O'Neal (12.5 reb)|Charles Barkley (11.7 reb)|Jayson Williams (12 reb)|Tim Duncan (12.4 reb)|
    |Dikembe Mutombo (11.6 reb)|Shaquille O'Neal 'n Dikembe Mutombo (11.4 reb)|Danny Fortson (11.6 reb)|Kevin Garnett (11.8 reb)|

    #### Assists
    |1996-97(CHI)|1997-98(CHI)|1998-99(SAS)|1999-00(LAL)|
    |------------|------------|------------|------------|
    |Mark Jackson (11.4 ast)|Rod Strickland (10.5 ast)|Jason Kidd (10.8 ast)|Jason Kidd (10.1 ast)|
    |John Stockton (10.5 ast)|Jason Kidd (9.1 ast)|Rod Strickland (9.9 ast)|Nick Van Exel (9 ast)|
    |Kevin Johnson (9.3 ast)|Mark Jackson (8.7 ast)|Stephon Marbury (8.9 ast)|Sam Cassel (9 ast)|
    |Jason Kidd (9 ast)|Stephon Marbury (8.6 ast)|Gary Payton (8.7 ast)|Terrel Brandon (8.9 ast)|
    |Rod Strickland (8.9 ast)|John Stockton (8.5 ast)|Terrel Brandon (8.6 ast)|Gary Payton (8.9 ast)|
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Analysing 2000's""")
    return


@app.cell
def _(nba_data):
    players_00s = nba_data.sql("SELECT * FROM self WHERE season like '200%'")
    season_2000_01 = players_00s.sql("SELECT * FROM self WHERE season like '2000-01'")
    season_2001_02 = players_00s.sql("SELECT * FROM self WHERE season like '2001-02'")
    season_2002_03 = players_00s.sql("SELECT * FROM self WHERE season like '2002-03'")
    season_2003_04 = players_00s.sql("SELECT * FROM self WHERE season like '2003-04'")
    season_2004_05 = players_00s.sql("SELECT * FROM self WHERE season like '2004-05'")
    season_2005_06 = players_00s.sql("SELECT * FROM self WHERE season like '2005-06'")
    season_2006_07 = players_00s.sql("SELECT * FROM self WHERE season like '2006-07'")
    season_2007_08 = players_00s.sql("SELECT * FROM self WHERE season like '2007-08'")
    season_2008_09 = players_00s.sql("SELECT * FROM self WHERE season like '2008-09'")
    season_2009_10 = players_00s.sql("SELECT * FROM self WHERE season like '2009-10'")
    return


@app.cell
def _():
    #season_2000_01.sql("SELECT player_name, age, gp, pts, reb, ast  FROM self ORDER BY pts DESC")
    #season_2000_01.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY reb DESC")
    #season_2000_01.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY ast DESC")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    #### Points
    |2000-01(LAL)|2001-02(LAL)|2002-03(SAS)|2003-04(DET)|2004-05(SAS)|2005-06(MIA)|2006-07(SAS)|2007-08(BOS)|2008-09(LAL)|2009-10(LAL)|
    |------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
    |Allen Iverson (31.1 pts)   |Allen Iverson (31.4 pts)   |Tracy MacGrady (32.1 pts)  |Tracy McGrady (28 pts)    |Allen Iverson (30.7 pts)|Kobe Bryant (35.4 pts)|Kobe Bryant (31.6 pts)|LeBron James (30 pts)|Dwayne Wade (30.2 pts)|Kevin Durant (30.1 pts)|
    |Jerry Stackhouse (29.8 pts)|Shaquille O`Neal (27.2 pts)|Kobe Bryant (30 pts)       |Allen Iverson (26.4 pts)  |Kobe Bryant (27.6 pts)|Allen Iverson (33 pts)|Carmelo Anthony (28.9 pts)|Kobe Bryant (28.3 pts)|LeBron James (28.4 pts)|LeBron James (29.7 pts)|
    |Shaquille O'Neal (28.7 pts)|Paul Pierce (26.1 pts)     |Allen Iverson (27.6 pts)   |Kevin Garnett (24.2 pts)  |LeBron James (27.2 pts)|LeBron James (31.4 pts)|Gilbert Arenas (28.4 pts)|Allen Iverson (26.4 pts)|Kobe Bryant (26.8 pts)|Carmelo Anthony (28.2 pts)|
    |Kobe Bryant (28.5 pts)     |Tracy McGrady (25.6 pts)   |Shaquille O'Neal (27.5 pts)|Peja Stojakovic (24.2 pts)|Dirk Nowitzki (26.1 pts)|Gilbert Arenas (29.3 pts)|Dwayne Wade (27.4 pts)|Carmelo Anthony (25.7 pts)|Dirk Nowitzki (25.9 pts)|Kobe Bryant (27 pts)|
    |Vince Carter(27.6 pts)     |Tim Duncan (25.5 pts)      |Paul Pierce (25.9 pts)     |Kobe Bryant (24 pts)      |Amar'e Stoudemire (26 pts)|Dwayne Wade (27.2 pts)|LeBron James (27.3 pts)|Amar'e Stoudemire (25.2 pts)|Danny Granger (25.8 pts)|Dwayne Wade (26.6 pts)|

    #### Rebounds
    |2000-01(LAL)|2001-02(LAL)|2002-03(SAS)|2003-04(DET)|2004-05(SAS)|2005-06(MIA)|2006-07(SAS)|2007-08(BOS)|2008-09(LAL)|2009-10(LAL)|
    |------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
    |Danny Fortson (16.3 reb)|Ben Wallace (13 reb)|Ben Wallace (15.4 reb)|Kevin Garnett (13.9 reb)|Kevin Garnett (13.5 reb)|Kevin Garnett(12.7 reb)|Kevin Garnett(12.8 reb)|Dwight Howard(14.2 reb)|Dwight Howard(13.8 reb)|Dwight Howard(13.2 reb)|
    |Dikembe Mutombo (13.5 reb)|Tim Duncan (12.7 reb)|Kevin Garnett (13.4 reb)|Ben Wallace (12.4 reb)|Ben Wallace (12.2 reb)|Dwight Howard(12.5 reb)|Tyson Chandler(12.4 reb)|Marcus Camby(13.1 reb)|Troy Murphy(11.8 reb)|Marcus Camby(11.8 reb)|
    |Ben Wallace (13.2 reb)|Kevin Garnett (12.1 reb)|Tim Duncan (12.9 reb)|Tim Duncan (12.4 reb)|Shawn Marion (11.3 reb)|Marcus Camby(11.9 reb)|Dwight Howard(12.3 reb)|Chris Kaman(12.7 reb)|David Lee(11.7 reb)|David Lee(11.7 reb)|
    |Shaquille O'Neal (12.7 reb)|Danny Fortson (11.7 reb)|Elton Brand (11.3 reb)|Erick Dampier (12 reb)|Tim Duncan (11.1 reb)|Shawn Marion(11.8 reb)|Carlos Boozer(11.7 reb)|Tyson Chandler(11.7 reb)|Andris Biedrins(11.2 reb)|Zach Randolph(11.7 reb)|
    |Tim Duncan (12.2 reb)|Elton Brand (11.6 reb)|Shaquille O'Neal (11.1 reb)|Shaquille O'Neal (11.5 reb)|Emeka Okafor (10.9 reb)|Ben Wallace(11.3 reb)|Marcus Camby(11.7 reb)|Tim Duncan(11.3 reb)|Marcus Camby(11.1 reb)|Pau Gasol(11.3 reb)|

    #### Assists
    |2000-01(LAL)|2001-02(LAL)|2002-03(SAS)|2003-04(DET)|2004-05(SAS)|2005-06(MIA)|2006-07(SAS)|2007-08(BOS)|2008-09(LAL)|2009-10(LAL)|
    |------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
    |Jason Kidd (9.8 ast)|Andre Miller (10.9 ast)|Jason Kidd (8.9 ast)|Jason Kidd (9.2 ast)|Steve Nash (11.5 ast)|Steve Nash (10.5 ast)|Steve Nash (11.6 ast)|Chris Paul (11.6 ast)|Chris Paul (11 ast)|Steve Nash (11 ast)|
    |John Stockton 8.7 ast)|Jason Kidd (9.9 ast)|Jason Williams (8.3 ast)|Stephon Marbury (8.9 ast)|Brevin Knight (9 ast)|Baron Davis (8.9 ast)|Deron Williams (9.3 ast)|Steve Nash (11.1 ast)|Deron Williams (10.7 ast)|Chris Paul (10.7 ast)|
    |Nick Van Exel (8.5 ast)|Gary Payton (9 ast)|Gary Payton (8.3 ast)|Steve Nash(8.8 ast)|Jason Kidd (8.3 ast)|Brevin Knight (8.8 ast)|Jason Kidd (9.2 ast)|Deron Williams (10.5 ast)|Gilbert Arenas(10 ast)|Deron Williams (10.5 ast)|
    |Mike Bibby (8.4 ast)|Baron Davis (8.5 ast)|Stephon Marbury (8.1 ast)|Baron Davis (7.5 ast)|Stephon Marbury ( 8.1 ast)|Chauncey Billups (8.6 ast)|Chris Paul (8.9 ast)|Jason Kidd (10.1 ast)|Steve Nash(9.7 ast)|Rajon Rondo (9.8 ast)|
    |Gary Payton (8.1 ast)|Terrel Brandon (8.3 ast)|John Stockton (7.7 ast)|Sam Cassell (7.3 ast)|Allen Iverson (7.9 ast)|Jason Kidd (8.4 ast)|Baron Davis (8.1 ast)|Jammal Tinsley (8.4 ast)|Jose Calderon (8.9 ast)|Jason Kidd (9.1 ast)|
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Analysing 2010`s""")
    return


@app.cell
def _(nba_data):
    players_10s = nba_data.sql("SELECT * FROM self WHERE season like '201%'")
    season_2010_11 = players_10s.sql("SELECT * FROM self WHERE season like '2010-11'")
    season_2011_12 = players_10s.sql("SELECT * FROM self WHERE season like '2011-12'")
    season_2012_13 = players_10s.sql("SELECT * FROM self WHERE season like '2012-13'")
    season_2013_14 = players_10s.sql("SELECT * FROM self WHERE season like '2013-14'")
    season_2014_15 = players_10s.sql("SELECT * FROM self WHERE season like '2014-15'")
    season_2015_16 = players_10s.sql("SELECT * FROM self WHERE season like '2015-16'")
    season_2016_17 = players_10s.sql("SELECT * FROM self WHERE season like '2016-17'")
    season_2017_18 = players_10s.sql("SELECT * FROM self WHERE season like '2017-18'")
    season_2018_19 = players_10s.sql("SELECT * FROM self WHERE season like '2018-19'")
    season_2019_20 = players_10s.sql("SELECT * FROM self WHERE season like '2019-20'")
    return


@app.cell
def _():
    #season_2010_11.sql("SELECT player_name, age, gp, pts, reb, ast  FROM self ORDER BY pts DESC")
    #season_2010_11.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY reb DESC")
    #season_2010_11.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY ast DESC")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    #### Points
    |2010-11(DAL)|2011-12(MIA)|2012-13(MIA)|2013-14(SAS)|2014-15(GSW)|2015-16(CAV)|2016-17(GSW)|2017-18(GSW)|2018-19(TOR)|2019-20(LAL)|
    |------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
    |Kevin Durant(27.7 pts)|Kevin Durant(28 pts)|Carmelo Anthony(28.7 pts)|Kevin Durant(32 pts)|Russel Westbrook(28.1 pts)|Stephen Curry(30.1 pts)|Russel Westbrook(31.6 pts)|James Harden(30.4 pts)|James Harden(36.1 pts)|James Harden(34.3 pts)|
    |LeBron James(26.7 pts)|Kobe Bryant(27.9 pts)|Kevin Durant(28.1 pts)|Carmelo Anthony(27.4 pts)|James Harden(27.4 pts)|James Harden(29 pts)|James Harden(29.1 pts)|Anthony Davis(28.1 pts)|Paul George(28 pts)|Bradley Beal(30.5 pts)|
    |Carmelo Anthony(25.6 pts)|LeBron James(27.1 pts)|Kobe Bryant(27.3 pts)|LeBron James(27.1 pts)|Kevin Durant(25.4 pts)|Kevin Durant(28.2 pts)|Isaiah Thomas(28.9 pts)|LeBron James(27.5 pts)|Giannis Antetokounmpo(27.7 pts)|Damian Lillard(30 pts)|
    |Dwayne Wade(25.5 pts)|Kevin Love(26 pts)|LeBron James(26.8 pts)|Kevin Love(26.1 pts)|LeBron James(25.3 pts)|DeMarcus Cousins(26.9 pts)|Anthony Davis(28 pts)|Damian Lillard(26.9 pts)|Joel Embiid(27.5 pts)|Trae Young(29.6 pts)|
    |Kobe Bryant(25.3 pts)|Russel Westbrook(23.6 pts)|James Harden(25.9 pts)|James Harden(25.4 pts)|Anthony Davis(24.4 pts)|LeBron James(25.3 pts)|DeMar DeRozan(27.3 pts)|Giannis Antetokounmpo(26.9 pts)|LeBron James(27.4 pts)|Giannis Antetokounmpo(29.5 pts)|

    #### Rebounds
    |2010-11(DAL)|2011-12(MIA)|2012-13(MIA)|2013-14(SAS)|2014-15(GSW)|2015-16(CAV)|2016-17(GSW)|2017-18(GSW)|2018-19(TOR)|2019-20(LAL)|
    |------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
    |Kevin Love(15.2 reb)|Dwight Howard(14.5 reb)|Anderson Varejão(14.4 reb)|DeAndre Jordan(13.6 reb)|DeAndre Jordan(15 reb)|Andre Drummond(14.8 reb)|Hassan Whiteside(14.1 reb)|Andre Drummond(16 reb)|Andre Drummond(15.6 reb)|Andre Drummond(15.2 reb)|
    |Dwight Howard(14.1 reb)|Kevin Love (13.3 reb)|Kevin Love(14 reb)|Andre Drummond(13.2 reb)|Andre Drummond(13.5 reb)|DeAndre Jordan(13.8 reb)|DeAndre Jordan(13.8 reb)|DeAndre Jordan(15.2 reb)|Joel Embiid(13.6 reb)|Clint Capela(13.8 reb)|
    |Zach Randolph(12.2 reb)|Andrew Bynum(11.8 reb)|Dwight Howard(12.4 reb)|Kevin Love(12.5 reb)|DeMarcus Cousins(12.7 reb)|Hassan Whiteside(11.8 reb)|Andre Drummond(13.8 reb)|DeMarcus Cousins(12.9 reb)|DeAndre Jordan(13.1 reb)|Giannis Antetokounmpo(13.6 reb)|
    |Blake Griffin(12.1 reb)|Anderson Varejão(11.5 reb)|Nikola Vucevic(11.9 reb)|Dwight Howard(12.2 reb)|Pau Gasol(11.8 reb)|Dwight Howard(11.8 reb)|Rudy Gobert(12.8 reb)|Dwight Howard(12.5 reb)|Rudy Gobert(12.9 reb)|Hassan Whiteside(13.5 reb)|
    |Reggie Evans(11.5 reb)|Kris Humphries & DeMarcus Cousins(11 reb)|Omer Asik(11.7 reb)|DeMarcus Cousins(11.7 reb)|Tyson Chandler(11.5 reb)|DeMarcus Cousins(11.5 reb)|Dwight Howard(12.7 reb)|Karl-Anthony Towns(12.3 reb)|Clint Capela(12.7 reb)|Rudy Gobert(13.5 reb)|

    #### Assists
    |2010-11(DAL)|2011-12(MIA)|2012-13(MIA)|2013-14(SAS)|2014-15(GSW)|2015-16(CAV)|2016-17(GSW)|2017-18(GSW)|2018-19(TOR)|2019-20(LAL)|
    |------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
    |Steve Nash(11.4 ast)|Rajon Rondo(11.7 ast)|Rajon Rondo(11.1 ast)|Chris Paul(10.7 ast)|Chris Paul(10.2 ast)|Rajon Rondo(11.7 ast)|James Harden(11.2 ast)|Russell Westbrook(10.3 ast)|Russell Westbrook(10.7 ast)|LeBron James(10.2 ast)|
    |Rajon Rondo(11.2 ast)|Steve Nash(10.7 ast)|Chris Paul(9.7 ast)|Rajon Rondo(9.8 ast)|John Wall(10 ast)|Russell Westbrook(10.4 ast)|John Wall(10.7 ast)|John Wall(9.6 ast)|John Wall(8.7 ast)|Trae Young(9.3 ast)|
    |Deron Williams(10.3 ast)|Chris Paul(9.1 ast)|Greivis Vasquez(9 ast)|John Wall(8.8 ast)|Ty Lawson(9.6 ast)|John Wall(10.2 ast)|Russell Westbrook(10.4 ast)|LeBron James(9.1 ast)|Kyle Lowry(8.7 ast)|Luka Doncic(8.8 ast)|
    |Chris Paul(9.8 ast)|Jose Calderon(8.8 ast)|Jrue Holiday(8 ast)|Ty Lawson(8.8 ast)|Ricky Rubio(8.8 ast)|Chris Paul(10 ast)|Chris Paul(9.2 ast)|James Harden(8.8 ast)|LeBron James(8.3 ast)|Ricky Rubio(8.8 ast)|
    |Jose Calderon(8.9 ast)|Deron Williams(8.7 ast)|Deron Williams(7.7 ast)|Kendall Marshall(8.8 ast)|Russell Westbrook(8.6 ast)|Ricky Rubio(8.7 ast)|Ricky Rubio(9.1 ast)|Rajon Rondo(8.2 ast)|Jeff Teague(8.2 ast)|Ben Simmons(8 ast)|
    """
    )
    return


@app.cell
def _(mo):
    mo.md(r"""## Analysing 2020's""")
    return


@app.cell
def _(nba_data):
    players_20s = nba_data.sql("SELECT * FROM self WHERE season like '202%'")
    season_2020_21 = players_20s.sql("SELECT * FROM self WHERE season like '2020-21'")
    season_2021_22 = players_20s.sql("SELECT * FROM self WHERE season like '2021-22'")
    season_2022_23 = players_20s.sql("SELECT * FROM self WHERE season like '2022-23'")
    return


@app.cell
def _():
    #season_2020_21.sql("SELECT player_name, age, gp, pts, reb, ast  FROM self ORDER BY pts DESC")
    #season_2020_21.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY reb DESC")
    #season_2020_21.sql("SELECT player_name, age, gp, pts, reb, ast FROM self ORDER BY ast DESC")
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    #### Points
    |2020-21(MIL)|2021-22(GSW)|2022-23(DEN)|
    |------------|------------|------------|
    |Stephen Curry(32 pts)|Joel Embiid(30.6 pts)|Joel Embiid(33.1 pts)|
    |Bradley Beal(31.3 pts)|LeBron James(30.3 pts)|Luka Doncic(32.4 pts)|
    |Damian Lillard(28.8 pts)|Giannis Antetokounmpo(29.9 pts)|Damian Lillard(32.2 pts)|
    |Joel Embiid(28.5 pts)|Kevin Durant(29.9 pts)|Shai Gilgeous-Alexander(31.4 pts)|
    |Giannis Antetokounmpo(28.1 pts)|Luka Doncic(28.4 pts)|Giannis Antetokounmpo(31.1 pts)|

    #### Rebounds
    |2020-21(MIL)|2021-22(GSW)|2022-23(DEN)|
    |------------|------------|------------|
    |Clint Capela(14.3 reb)|Rudy Gobert(14.7 reb)|Anthony Davis(12.5 reb)|
    |Rudy Gobert(13.5 reb)|Nikola Jokic(13.8 reb)|Domantas Sabonis(12.3 reb)|
    |Jonas Valaciunas(12.5 reb)|Domantas Sabonis(12.1 reb)|Nikola Jokic(11.8 reb)|
    |Domantas Sabonis(12 reb)|Jaylen Hoard(12 reb)|Giannis Antetokounmpo(11.8 reb)|
    |Andre Drummond(12 reb)|Clint Capela(11.9 reb)|Rudy Gobert(11.6 reb)|

    #### Assists
    |2020-21(MIL)|2021-22(GSW)|2022-23(DEN)|
    |------------|------------|------------|
    |Russel Westbrook(11.7 ast)|Chris Paul(10.8 ast)|James Harden(10.7 ast)|
    |James Harden(10.8 ast)|James Harden(10.3 ast)|Tyrese Haliburton(10.4 ast)|
    |Trae Young(9.4 ast)|Trae Young(9.7 ast)|Trae Young(10.2 ast)|
    |Draymond Green(8.9 ast)|Dejount Murray(9.2 ast)|Nikola Jokic(9.8 ast)|
    |Chris Paul(8.9 ast)|Luka Doncic(8.7 ast)|Chris Paul(8.9 ast)|
    """
    )
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## In Conclusion
    The list of whom has more appearances at top 5 for each category in history is shown below:

    ### Points:
    - LeBron James: 15🥇
    - Kobe Bryant: 12🥈
    - Allen Iverson: 8🥉
    - Kevin Durant: 8🥉
    - James Harden: 8🥉
    - Shaquille O'Neal: 7
    - Giannis Antetokounmpo: 6
    - Carmelo Anthony: 6
    - Dwayne Wade: 5
    - Joel Embiid: 4

    ### Rebounds:
    - Dwight Howard: 11🥇
    - Andre Drummond: 8🥈
    - Tim Duncan: 8🥈
    - Kevin Garnett: 7🥉
    - Ben Wallace: 6
    - Shaquille O'Neal: 6
    - DeAndre Jordan: 6
    - Rudy Gobert: 6
    - Dikembe Mutombo: 5
    - Marcus Camby: 5

    ### Assists:
    - Chris Paul: 14🥇
    - Jason Kidd: 12🥈
    - Steve Nash: 9🥉
    - Rajon Rondo: 7
    - Deron Williams: 7
    - Russel Westbrook: 6
    - John Wall: 6
    - James: Harden: 5
    - Stephon Marbury: 5
    - Gary Payton: 5
    """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
    ## Compare efficiency stats (TS% vs usage%) - do volume scorers sacrifice efficiency?
    True Shooting Percentage is a mesaure to see the efficiency of shooting(field goal, three points and free throws)

    Usage Percentage is the statistics of team plays that the player have contributed, the ball has passed throught him.
    """
    )
    return


@app.cell
def _(nba_data, pl):
    volume_scorers_all_time = pl.LazyFrame(data=nba_data['player_name','pts','ts_pct','usg_pct','season'].sort('pts',descending=True))
    top_true_shooting = pl.LazyFrame(data=nba_data['player_name','pts','ts_pct','usg_pct','season'].sort('ts_pct',descending=True))
    top_usage_rate = pl.LazyFrame(data=nba_data['player_name','pts','ts_pct','usg_pct','season'].sort('usg_pct',descending=True))
    return top_true_shooting, top_usage_rate


@app.cell
def _(nba_data, pl):
    volume_rebounders_all_time = pl.LazyFrame(data=nba_data['player_name','reb','ts_pct','usg_pct','season'].sort('reb',descending=True))
    volume_assisters_all_time = pl.LazyFrame(data=nba_data['player_name','ast','ts_pct','usg_pct','season'].sort('ast',descending=True))
    return


@app.cell
def _(pl, top_usage_rate):
    # Filtering players by points, more than 5 and 10
    #top_usage_rate.filter(pl.col('pts') > 5).collect()
    top_usage_rate.filter(pl.col('pts') > 10).collect()
    return


@app.cell
def _(pl, top_true_shooting):
    # Filtering players by points, more than 5, 10, 20
    #top_true_shooting.filter(pl.col('pts') > 5).collect()
    #top_true_shooting.filter(pl.col('pts') > 10).collect()
    top_true_shooting.filter(pl.col('pts') > 20).collect()
    return


@app.cell
def _(mo):
    mo.md(
        r"""
    ## Identify most improved players across seasons (biggest jump in points/rebounds/assists).
    Let's verify per best top 5 players of each category in history

    ### Points
    - James Harden: 36.1 pts(2018-19)
    - Kobe Bryant: 35.4 pts(2005-06)
    - Joel Embiid: 33.1 pts(2022-23)
    - Allen Iverson: 33 pts(2005-06)
    - Luka Doncic: 32.4 pts(2022-23)

    ### Rebounds
    - Danny Fortson: 16.3 reb(2000-01)
    - Dennis Rodman: 16.1 reb(1996-97)
    - Andre Drummond: 16 reb(2017-18)
    - Ben Wallace: 15.4 reb(2002-03)
    - Kevin Love & DeAndre Jordan: 15.2 reb(2010-11 & 2017-18)

    ### Assists
    - Rajon Rondo: 11.7 ast(2011-12)
    - Russell Westbrook: 11.7 ast(2020-21)
    - Steve Nash: 11.6 ast(2006-07)
    - Chris Paul: 11.6 ast(2007-08)
    - Mark Jackson: 11.4 ast(1996-97)
    """
    )
    return


@app.cell
def _():
    #volume_scorers_all_time.collect()
    #volume_rebounders_all_time.collect()
    #volume_assisters_all_time.collect()
    return


@app.cell
def _(nba_data):
    james_harden = nba_data.sql("SELECT pts,reb,ast,season FROM self WHERE player_name like 'James Harden' ORDER BY season")
    kobe_bryant = nba_data.sql("SELECT pts,reb,ast,season FROM self WHERE player_name like 'Kobe Bryant' ORDER BY season")
    joel_embiid = nba_data.sql("SELECT pts,reb,ast,season FROM self WHERE player_name like 'Joel Embiid' ORDER BY season")
    allen_iverson = nba_data.sql("SELECT pts,reb,ast,season FROM self WHERE player_name like 'Allen Iverson' ORDER BY season")
    luka_doncic = nba_data.sql("SELECT pts,reb,ast,season FROM self WHERE player_name like 'Luka Doncic' ORDER BY season")
    lebron_james = nba_data.sql("SELECT pts,reb,ast,season FROM self WHERE player_name like 'LeBron James' ORDER BY season")
    return (luka_doncic,)


@app.cell
def _(luka_doncic, sns):
    season = luka_doncic['season']
    basket_data = luka_doncic['pts']
    sns.set_theme(style='whitegrid')
    sns.lineplot(x=season, y=basket_data)
    return


if __name__ == "__main__":
    app.run()

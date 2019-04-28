import dash_core_components as dcc
import dash_html_components as html
import dash
from dash.dependencies import Input, Output, State
import pandas as pd
from flask import Flask
import os


server = Flask(__name__)
server.secret_key = os.environ.get('secret_key', 'secret')
app = dash.Dash(name = __name__, server = server)
app.config.supress_callback_exceptions = True



df = pd.read_csv('12.csv')
df = df.drop(['season','date'], axis = 'columns')
res = []
i = 0
for e in df.itertuples():
    if e.home_team_goal > e.away_team_goal :
          df.at[i,'res']= int(1)
          i = i+1
    elif e.home_team_goal == e.away_team_goal :
          df.at[i,'res']= int(0)
          i = i+1
    else :
          df.at[i,'res']= int(-1)
          i = i+1
from sklearn.model_selection import train_test_split
X = df.drop(['id','res','league_id','stage','match_api_id','home_team_goal','away_team_goal'], axis='columns')
y = df.res
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.99)
from sklearn.svm import SVC
model_s = SVC(C=5,gamma ='auto' )
print(X_train)
model_s.fit(X_train, y_train)
model_s.score(X_test, y_test)

from sklearn.linear_model import LinearRegression
model_l = LinearRegression()
model_l.fit(X_train,y_train)
country_list = [{'label': 'Belgium', 'value': '1'},
                {'label': 'England', 'value': '1729'},{'label': 'France', 'value': '4769'},
                {'label': 'Germany', 'value': '7809'},
                {'label': 'Italy', 'value': '10257'},
                {'label': 'Netherlands', 'value': '13274'},
                {'label': 'Poland', 'value': '15722'},
                {'label': 'Portugal', 'value': '17642'},
                {'label': 'Scotland', 'value': '19694'},
                {'label': 'Spain', 'value': '21518'},
                {'label': 'Switzerland', 'value': '24558'}]

t_value = [
    {'label': 'KRC Genk-GEN', 'value': '9987'},
    {'label': 'Beerschot AC-BAC', 'value': '9993'},
    {'label': 'SV Zulte-Waregem-ZUL', 'value': '10000'},
    {'label': 'Sporting Lokeren-LOK', 'value': '9994'},
    {'label': 'KSV Cercle Brugge-CEB', 'value': '9984'},
    {'label': 'RSC Anderlecht-AND', 'value': '8635'},
    {'label': 'KAA Gent-GEN', 'value': '9991'},
    {'label': 'RAEC Mons-MON', 'value': '9998'},
    {'label': 'FCV Dender EH-DEN', 'value': '7947'},
    {'label': 'Standard de Liège-STL', 'value': '9985'},
    {'label': 'KV Mechelen-MEC', 'value': '8203'},
    {'label': 'Club Brugge KV-CLB', 'value': '8342'},
    {'label': 'KSV Roeselare-ROS', 'value': '9999'},
    {'label': 'KV Kortrijk-KOR', 'value': '8571'},
    {'label': 'Tubize-TUB', 'value': '4049'},
    {'label': 'Royal Excel Mouscron-MOU', 'value': '9996'},
    {'label': 'KVC Westerlo-WES', 'value': '10001'},
    {'label': 'Sporting Charleroi-CHA', 'value': '9986'},
    {'label': 'Sint-Truidense VV-STT', 'value': '9997'},
    {'label': 'Lierse SK-LIE', 'value': '9989'},
    {'label': 'KAS Eupen-EUP', 'value': '6351'},
    {'label': 'Oud-Heverlee Leuven-O-H', 'value': '1773'},
    {'label': 'Waasland-Beveren-WAA', 'value': '8475'},
    {'label': 'KV Oostende-OOS', 'value': '8573'},
    {'label': 'Royal Excel Mouscron-MOP', 'value': '274581'},
    {'label': 'Manchester United-MUN', 'value': '10260'},
    {'label': 'Newcastle United-NEW', 'value': '10261'},
    {'label': 'Arsenal-ARS', 'value': '9825'},
    {'label': 'West Bromwich Albion-WBA', 'value': '8659'},
    {'label': 'Sunderland-SUN', 'value': '8472'},
    {'label': 'Liverpool-LIV', 'value': '8650'},
    {'label': 'West Ham United-WHU', 'value': '8654'},
    {'label': 'Wigan Athletic-WIG', 'value': '8528'},
    {'label': 'Aston Villa-AVL', 'value': '10252'},
    {'label': 'Manchester City-MCI', 'value': '8456'},
    {'label': 'Everton-EVE', 'value': '8668'},
    {'label': 'Blackburn Rovers-BLB', 'value': '8655'},
    {'label': 'Middlesbrough-MID', 'value': '8549'},
    {'label': 'Tottenham Hotspur-TOT', 'value': '8586'},
    {'label': 'Bolton Wanderers-BOL', 'value': '8559'},
    {'label': 'Stoke City-STK', 'value': '10194'},
    {'label': 'Hull City-HUL', 'value': '8667'},
    {'label': 'Fulham-FUL', 'value': '9879'},
    {'label': 'Chelsea-CHE', 'value': '8455'},
    {'label': 'Portsmouth-POR', 'value': '8462'},
    {'label': 'Birmingham City-BIR', 'value': '8658'},
    {'label': 'Wolverhampton Wanderers-WOL', 'value': '8602'},
    {'label': 'Burnley-BUR', 'value': '8191'},
    {'label': 'Blackpool-BLA', 'value': '8483'},
    {'label': 'Swansea City-SWA', 'value': '10003'},
    {'label': 'Queens Park Rangers-QPR', 'value': '10172'},
    {'label': 'Norwich City-NOR', 'value': '9850'},
    {'label': 'Southampton-SOU', 'value': '8466'},
    {'label': 'Reading-REA', 'value': '9798'},
    {'label': 'Crystal Palace-CRY', 'value': '9826'},
    {'label': 'Cardiff City-CAR', 'value': '8344'},
    {'label': 'Leicester City-LEI', 'value': '8197'},
    {'label': 'Bournemouth-BOU', 'value': '8678'},
    {'label': 'Watford-WAT', 'value': '9817'},
    {'label': 'AJ Auxerre-AUX', 'value': '8583'},
    {'label': 'FC Nantes-NAN', 'value': '9830'},
    {'label': 'Girondins de Bordeaux-BOR', 'value': '9827'},
    {'label': 'SM Caen-CAE', 'value': '7819'},
    {'label': 'Le Havre AC-LEH', 'value': '9746'},
    {'label': 'OGC Nice-NIC', 'value': '9831'},
    {'label': 'Le Mans FC-LEM', 'value': '8682'},
    {'label': 'FC Lorient-LOR', 'value': '8689'},
    {'label': 'Olympique Lyonnais-LYO', 'value': '9748'},
    {'label': 'Toulouse FC-TOU', 'value': '9941'},
    {'label': 'AS Monaco-MON', 'value': '9829'},
    {'label': 'Paris Saint-Germain-PSG', 'value': '9847'},
    {'label': 'AS Nancy-Lorraine-NAN', 'value': '8481'},
    {'label': 'LOSC Lille-LIL', 'value': '8639'},
    {'label': 'Stade Rennais FC-REN', 'value': '9851'},
    {'label': 'Olympique de Marseille-MAR', 'value': '8592'},
    {'label': 'FC Sochaux-Montbéliard-SOC', 'value': '9874'},
    {'label': 'Grenoble Foot 38-GRE', 'value': '9855'},
    {'label': 'Valenciennes FC-VAL', 'value': '9873'},
    {'label': 'AS Saint-Étienne-ETI', 'value': '9853'},
    {'label': 'RC Lens-LEN', 'value': '8588'},
    {'label': 'Montpellier Hérault SC-MON', 'value': '10249'},
    {'label': 'US Boulogne Cote D\'Opale-BOU', 'value': '4170'},
    {'label': 'AC Arles-Avignon-ARL', 'value': '108893'},
    {'label': 'Stade Brestois 29-BRE', 'value': '8521'},
    {'label': 'AC Ajaccio-AJA', 'value': '8576'},
    {'label': 'Évian Thonon Gaillard FC-ETG', 'value': '4087'},
    {'label': 'Dijon FCO-DIJ', 'value': '9836'},
    {'label': 'Stade de Reims-REI', 'value': '9837'},
    {'label': 'SC Bastia-BAS', 'value': '7794'},
    {'label': 'ES Troyes AC-TRO', 'value': '10242'},
    {'label': 'En Avant de Guingamp-GUI', 'value': '9747'},
    {'label': 'FC Metz-MET', 'value': '8550'},
    {'label': 'Angers SCO-ANG', 'value': '8121'},
    {'label': 'GFC Ajaccio-GAJ', 'value': '6391'},
    {'label': 'FC Bayern Munich-BMU', 'value': '9823'},
    {'label': 'Hamburger SV-HAM', 'value': '9790'},
    {'label': 'Bayer 04 Leverkusen-LEV', 'value': '8178'},
    {'label': 'Borussia Dortmund-DOR', 'value': '9789'},
    {'label': 'FC Schalke 04-S04', 'value': '10189'},
    {'label': 'Hannover 96-HAN', 'value': '9904'},
    {'label': 'VfL Wolfsburg-WOL', 'value': '8721'},
    {'label': '1. FC Köln-FCK', 'value': '8722'},
    {'label': 'Eintracht Frankfurt-EFR', 'value': '9810'},
    {'label': 'Hertha BSC Berlin-HBE', 'value': '8177'},
    {'label': 'DSC Arminia Bielefeld-BIE', 'value': '9912'},
    {'label': 'SV Werder Bremen-WBR', 'value': '8697'},
    {'label': 'FC Energie Cottbus-COT', 'value': '8398'},
    {'label': 'TSG 1899 Hoffenheim-HOF', 'value': '8226'},
    {'label': 'Borussia Mönchengladbach-GLA', 'value': '9788'},
    {'label': 'VfB Stuttgart-STU', 'value': '10269'},
    {'label': 'Karlsruher SC-KAR', 'value': '8295'},
    {'label': 'VfL Bochum-BOC', 'value': '9911'},
    {'label': 'SC Freiburg-FRE', 'value': '8358'},
    {'label': '1. FC Nürnberg-NUR', 'value': '8165'},
    {'label': '1. FSV Mainz 05-MAI', 'value': '9905'},
    {'label': '1. FC Kaiserslautern-KAI', 'value': '8350'},
    {'label': 'FC St. Pauli-STP', 'value': '8152'},
    {'label': 'FC Augsburg-AUG', 'value': '8406'},
    {'label': 'Fortuna Düsseldorf-FDU', 'value': '8194'},
    {'label': 'SpVgg Greuther Fürth-GRF', 'value': '8357'},
    {'label': 'Eintracht Braunschweig-BRA', 'value': '9776'},
    {'label': 'SC Paderborn 07-PAD', 'value': '8460'},
    {'label': 'FC Ingolstadt 04-ING', 'value': '8234'},
    {'label': 'SV Darmstadt 98-DAR', 'value': '8262'},
    {'label': 'Atalanta-ATA', 'value': '8524'},
    {'label': 'Siena-SIE', 'value': '8551'},
    {'label': 'Cagliari-CAG', 'value': '8529'},
    {'label': 'Lazio-LAZ', 'value': '8543'},
    {'label': 'Catania-CAT', 'value': '8530'},
    {'label': 'Genoa-GEN', 'value': '10233'},
    {'label': 'Chievo Verona-CHI', 'value': '8533'},
    {'label': 'Reggio Calabria-REG', 'value': '8690'},
    {'label': 'Fiorentina-FIO', 'value': '8535'},
    {'label': 'Juventus-JUV', 'value': '9885'},
    {'label': 'Milan-ACM', 'value': '8564'},
    {'label': 'Bologna-BOL', 'value': '9857'},
    {'label': 'Roma-ROM', 'value': '8686'},
    {'label': 'Napoli-NAP', 'value': '9875'},
    {'label': 'Sampdoria-SAM', 'value': '9882'},
    {'label': 'Inter-INT', 'value': '8636'},
    {'label': 'Torino-TOR', 'value': '9804'},
    {'label': 'Lecce-LEC', 'value': '9888'},
    {'label': 'Udinese-UDI', 'value': '8600'},
    {'label': 'Palermo-PAL', 'value': '8540'},
    {'label': 'Bari-BAR', 'value': '9976'},
    {'label': 'Livorno-LIV', 'value': '8537'},
    {'label': 'Parma-PAR', 'value': '10167'},
    {'label': 'Cesena-CES', 'value': '9880'},
    {'label': 'Brescia-BRE', 'value': '9858'},
    {'label': 'Novara-NOV', 'value': '6269'},
    {'label': 'Pescara-PES', 'value': '9878'},
    {'label': 'Hellas Verona-VER', 'value': '9876'},
    {'label': 'Sassuolo-SAS', 'value': '7943'},
    {'label': 'Empoli-EMP', 'value': '8534'},
    {'label': 'Frosinone-FRO', 'value': '9891'},
    {'label': 'Carpi-CAP', 'value': '208931'},
    {'label': 'Vitesse-VIT', 'value': '8277'},
    {'label': 'FC Groningen-GRO', 'value': '8674'},
    {'label': 'Roda JC Kerkrade-ROD', 'value': '9803'},
    {'label': 'FC Twente-TWE', 'value': '8611'},
    {'label': 'Willem II-WII', 'value': '8525'},
    {'label': 'Ajax-AJA', 'value': '8593'},
    {'label': 'N.E.C.-NEC', 'value': '8464'},
    {'label': 'De Graafschap-GRA', 'value': '8526'},
    {'label': 'FC Utrecht-UTR', 'value': '9908'},
    {'label': 'PSV-PSV', 'value': '8640'},
    {'label': 'Heracles Almelo-HER', 'value': '9791'},
    {'label': 'Feyenoord-FEY', 'value': '10235'},
    {'label': 'Sparta Rotterdam-SPA', 'value': '8614'},
    {'label': 'ADO Den Haag-HAA', 'value': '10217'},
    {'label': 'FC Volendam-VOL', 'value': '6601'},
    {'label': 'SC Heerenveen-HEE', 'value': '10228'},
    {'label': 'AZ-ALK', 'value': '10229'},
    {'label': 'NAC Breda-NAC', 'value': '9761'},
    {'label': 'RKC Waalwijk-RKC', 'value': '10219'},
    {'label': 'VVV-Venlo-VEN', 'value': '9839'},
    {'label': 'Excelsior-EXC', 'value': '10218'},
    {'label': 'PEC Zwolle-ZWO', 'value': '6413'},
    {'label': 'SC Cambuur-CAM', 'value': '7788'},
    {'label': 'Go Ahead Eagles-GAE', 'value': '6433'},
    {'label': 'FC Dordrecht-DOR', 'value': '6631'},
    {'label': 'Wisła Kraków-WIS', 'value': '10265'},
    {'label': 'Polonia Bytom-POB', 'value': '8031'},
    {'label': 'Polonia Bytom-GOR', 'value': '8020'},
    {'label': 'Ruch Chorzów-CHO', 'value': '1601'},
    {'label': 'Legia Warszawa-LEG', 'value': '8673'},
    {'label': 'P. Warszawa-PWA', 'value': '2183'},
    {'label': 'Śląsk Wrocław-SLA', 'value': '8025'},
    {'label': 'Lechia Gdańsk-LGD', 'value': '8030'},
    {'label': 'Widzew Łódź-LOD', 'value': '8244'},
    {'label': 'Odra Wodzisław-ODR', 'value': '8242'},
    {'label': 'Lech Poznań-POZ', 'value': '2182'},
    {'label': 'GKS Bełchatów-BEL', 'value': '8569'},
    {'label': 'Arka Gdynia-ARK', 'value': '8322'},
    {'label': 'Jagiellonia Białystok-BIA', 'value': '1957'},
    {'label': 'Piast Gliwice-PIG', 'value': '8028'},
    {'label': 'Cracovia-CKR', 'value': '2186'},
    {'label': 'Korona Kielce-KKI', 'value': '8245'},
    {'label': 'Zagłębie Lubin-ZAG', 'value': '8021'},
    {'label': 'Widzew Łódź-WID', 'value': '8024'},
    {'label': 'Podbeskidzie Bielsko-Biała-POD', 'value': '8033'},
    {'label': 'Pogoń Szczecin-POG', 'value': '8023'},
    {'label': 'Zawisza Bydgoszcz-ZAW', 'value': '8027'},
    {'label': 'Górnik Łęczna-LEC', 'value': '8019'},
    {'label': 'Termalica Bruk-Bet Nieciecza-TBN', 'value': '177361'},
    {'label': 'FC Porto-POR', 'value': '9773'},
    {'label': 'CF Os Belenenses-BEL', 'value': '9807'},
    {'label': 'Sporting CP-SCP', 'value': '9768'},
    {'label': 'Trofense-TRO', 'value': '7992'},
    {'label': 'Vitória Guimarães-GUI', 'value': '7844'},
    {'label': 'Vitória Setúbal-SET', 'value': '10238'},
    {'label': 'FC Paços de Ferreira-FER', 'value': '6403'},
    {'label': 'SC Braga-BRA', 'value': '10264'},
    {'label': 'Amadora-AMA', 'value': '10213'},
    {'label': 'Académica de Coimbra-ACA', 'value': '10215'},
    {'label': 'Rio Ave FC-RA', 'value': '7841'},
    {'label': 'SL Benfica-BEN', 'value': '9772'},
    {'label': 'Leixões SC-LEI', 'value': '6421'},
    {'label': 'CD Nacional-NAC', 'value': '10214'},
    {'label': 'Naval 1° de Maio-NAV', 'value': '9809'},
    {'label': 'CS Marìtimo-MAR', 'value': '10212'},
    {'label': 'União de Leiria, SAD-ULE', 'value': '9771'},
    {'label': 'S.C. Olhanense-OLH', 'value': '2033'},
    {'label': 'Portimonense-POR', 'value': '9765'},
    {'label': 'SC Beira Mar-B-M', 'value': '10211'},
    {'label': 'Feirense-FEI', 'value': '4064'},
    {'label': 'Gil Vicente FC-GV', 'value': '9764'},
    {'label': 'Moreirense FC-MOR', 'value': '8348'},
    {'label': 'Estoril Praia-EST', 'value': '7842'},
    {'label': 'FC Arouca-ARO', 'value': '158085'},
    {'label': 'FC Penafiel-PEN', 'value': '6547'},
    {'label': 'Boavista FC-BOA', 'value': '8613'},
    {'label': 'Uniao da Madeira-MAD', 'value': '6367'},
    {'label': 'Tondela-TON', 'value': '188163'},
    {'label': 'Falkirk-FAL', 'value': '8596'},
    {'label': 'p-RAN', 'value': '8548'},
    {'label': 'Heart of Midlothian-HEA', 'value': '9860'},
    {'label': 'Motherwell-MOT', 'value': '9927'},
    {'label': 'Kilmarnock-KIL', 'value': '8597'},
    {'label': 'Hibernian-HIB', 'value': '10251'},
    {'label': 'Aberdeen-ABE', 'value': '8485'},
    {'label': 'Inverness Caledonian Thistle-INV', 'value': '8066'},
    {'label': 'Celtic-CEL', 'value': '9925'},
    {'label': 'St. Mirren-MIR', 'value': '9800'},
    {'label': 'Hamilton Academical FC-HAM', 'value': '8429'},
    {'label': 'Dundee United-DUU', 'value': '9938'},
    {'label': 'St. Johnstone FC-JOH', 'value': '8467'},
    {'label': 'Dunfermline Athletic-DUN', 'value': '8457'},
    {'label': 'Dundee FC-DUF', 'value': '8284'},
    {'label': 'Ross County FC-ROS', 'value': '8649'},
    {'label': 'Partick Thistle F.C.-PAR', 'value': '8426'},
    {'label': 'Valencia CF-VAL', 'value': '10267'},
    {'label': 'RCD Mallorca-MAL', 'value': '8661'},
    {'label': 'CA Osasuna-OSA', 'value': '8371'},
    {'label': 'Villarreal CF-VIL', 'value': '10205'},
    {'label': 'RC Deportivo de La Coruña-COR', 'value': '9783'},
    {'label': 'Real Madrid CF-REA', 'value': '8633'},
    {'label': 'CD Numancia-NUM', 'value': '8388'},
    {'label': 'FC Barcelona-BAR', 'value': '8634'},
    {'label': 'Racing Santander-SAN', 'value': '8696'},
    {'label': 'Sevilla FC-SEV', 'value': '8302'},
    {'label': 'Real Sporting de Gijón-SPG', 'value': '9869'},
    {'label': 'Getafe CF-GET', 'value': '8305'},
    {'label': 'Real Betis Balompié-BET', 'value': '8603'},
    {'label': 'RC Recreativo-HUE', 'value': '8479'},
    {'label': 'RCD Espanyol-ESP', 'value': '8558'},
    {'label': 'Real Valladolid-VAL', 'value': '10281'},
    {'label': 'Athletic Club de Bilbao-BIL', 'value': '8315'},
    {'label': 'UD Almerìa-ALM', 'value': '9865'},
    {'label': 'Atlético Madrid-AMA', 'value': '9906'},
    {'label': 'Málaga CF-MAL', 'value': '9864'},
    {'label': 'Xerez Club Deportivo-XER', 'value': '9868'},
    {'label': 'Real Zaragoza-ZAR', 'value': '8394'},
    {'label': 'CD Tenerife-TEN', 'value': '9867'},
    {'label': 'Hércules Club de Fútbol-HER', 'value': '10278'},
    {'label': 'Levante UD-LEV', 'value': '8581'},
    {'label': 'Real Sociedad-SOC', 'value': '8560'},
    {'label': 'Granada CF-GRA', 'value': '7878'},
    {'label': 'Rayo Vallecano-RAY', 'value': '8370'},
    {'label': 'RC Celta de Vigo-CEL', 'value': '9910'},
    {'label': 'Elche CF-ELC', 'value': '10268'},
    {'label': 'SD Eibar-EIB', 'value': '8372'},
    {'label': 'Córdoba CF-COR', 'value': '7869'},
    {'label': 'UD Las Palmas-LAS', 'value': '8306'},
    {'label': 'Grasshopper Club Zürich-GRA', 'value': '9956'},
    {'label': 'AC Bellinzona-BEL', 'value': '6493'},
    {'label': 'BSC Young Boys-YB', 'value': '10192'},
    {'label': 'FC Basel-BAS', 'value': '9931'},
    {'label': 'FC Aarau-AAR', 'value': '9930'},
    {'label': 'FC Sion-SIO', 'value': '10179'},
    {'label': 'FC Luzern-LUZ', 'value': '10199'},
    {'label': 'FC Vaduz-VAD', 'value': '9824'},
    {'label': 'Neuchâtel Xamax-XAM', 'value': '7955'},
    {'label': 'FC Zürich-ZUR', 'value': '10243'},
    {'label': 'FC St. Gallen-GAL', 'value': '10190'},
    {'label': 'FC Thun-THU', 'value': '10191'},
    {'label': 'Servette FC-SER', 'value': '9777'},
    {'label': 'FC Lausanne-Sports-LAU', 'value': '7730'},
    {'label': 'Lugano-LUG', 'value': '7896'}]
app.css.append_css({'external_url': 'https://cdn.rawgit.com/plotly/dash-app-stylesheets/2d266c578d2a6e8850ebce48fdb52759b2aef506/stylesheet-oil-and-gas.css'})  # noqa: E501
app.css.append_css({'external_url': 'https://raw.githubusercontent.com/shashanktmk007/MATCH_PREDICTION-/master/style.css'})  # noqa: E501
app.layout = html.Div([
    html.H1("Soccer Predictor ",className="row"),
    html.Br(),
    #   html.H1(t_value),
    html.Div([
        html.Div([
        dcc.Dropdown(
            id='t_sel1',
            options=t_value,
            multi=False,
            placeholder='Select Team 1'
        )], className='three columns'),
         html.Div([
        dcc.Dropdown(
            id='t_sel2',
            options=t_value,
            multi=False,
            placeholder='Select Team 2'
        )], className='three columns'), html.Div([
        dcc.Dropdown(
            id='country_sel',
            options=country_list,
            multi=False,
            placeholder='Select Match Country'
        )], className='three columns')
    ],className="row"),
    html.Br(),
    html.Br(),
    html.Button(id='submit-button', n_clicks=0, children='Submit'),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div([
            html.Div([
                html.P('Support Vector Machine'), html.P('Stats : ', id='SVM_P')
            ], className='three columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'})
        ],),
        html.Div([
            html.P('Linear Regression'), html.P('Stats : ', id='LR_P')
        ] ,className='three columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'}),
        html.Div([
            html.P('XGBoost'), html.P('Stats : ', id='XG_P')
        ], className='three columns',style={'borderColor':' #57c5f7','borderWidth': 'medium','borderStyle': 'solid','borderRadius': '3.5%','backgroundColor': '#b0b0b05c','padding':'3%','textAlign': 'center','color': 'black'})
    ],className="row")
])

@app.callback(Output('SVM_P', 'children'),
              [Input('submit-button', 'n_clicks'), Input('country_sel', 'value')],
              [State('t_sel1', 'value'),
               State('t_sel2', 'value')])
def update_svm(n_clicks, c_val, input1, input2):
    if n_clicks > 0:
        a = calc_svm(c_val, input1, input2)
        if c_val is None or input1 is None or input2 is None:
            return 'ERROR All 3 values are required'
        elif input1 == input2:
            # print('values of country are equal ')
            #            dcc.ConfirmDialog(message="Select Country")
            return 'ERROR Same Team Selected '
        else:
            if a == 1:
                return 'Stats : Won'
            elif a == 0:
                return 'Stats : Draw'
            elif a == -1:
                return 'Stats : Lose'
    else:
        return 'Stats : '


@app.callback(Output('XG_P', 'children'),
              [Input('submit-button', 'n_clicks'), Input('country_sel', 'value')],
              [State('t_sel1', 'value'),
               State('t_sel2', 'value')])
def update_xg(n_clicks, c_val, input1, input2):
    if n_clicks > 0:
        a = calc_xg(c_val, input1, input2)
        # print(c_val,input1,input2)
        if c_val is None or input1 is None or input2 is None:
            return 'ERROR All 3 values are required'
        elif input1 == input2:
            # print('values of country are equal ')
            #            dcc.ConfirmDialog(message="Select Country")
            return 'ERROR Same Team Selected '
        else:
            if a == 1:
                return 'Stats : Won'
            elif a == 0:
                return 'Stats : Draw'
            elif a == -1:
                return 'Stats : Lose'
    else:
        return 'Stats : '


@app.callback(Output('LR_P', 'children'),
              [Input('submit-button', 'n_clicks'), Input('country_sel', 'value')],
              [State('t_sel1', 'value'),
               State('t_sel2', 'value')])
def update_lr(n_clicks, c_val, input1, input2):
    if n_clicks > 0:
        a = calc_lr( c_val, input1, input2)
        if c_val is None or input1 is None or input2 is None:
            return 'ERROR All 3 values are required'
        elif input1 == input2:
            # print('values of country are equal ')
            #            dcc.ConfirmDialog(message="Select Country")
            return 'ERROR Same Team Selected '
        else:
            if a == 1:
                return 'Stats : Won'
            elif a == 0:
                return 'Stats : Draw'
            elif a == -1:
                return 'Stats : Lose'
           # else :
            #    return 'Stats : Draw'

    else:
        return 'Stats : '


def calc_xg(c_val, input1, input2):
     return model_s.predict([[c_val, input1, input2]])



def calc_svm(c_val, input1, input2):
    return model_s.predict([[c_val, input1, input2]])


def calc_lr(c_val, input1, input2):
    return model_s.predict([[c_val, input1, input2]])

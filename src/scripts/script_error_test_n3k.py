# this is a manual script test of N3k with distance comparison score using NLTK
# this version is verbose to check errors
# NB: obsolete, now we use selenium for raw html scraping 

# measure execution time
#    + https://datatofish.com/measure-time-to-run-python-script/ 
import time
start_time = time.time()

# debug module imports
import os
print(
    "Python Current Working directory = " + str(os.getcwd())
)

# run at ".." level
from context import get_python_run_context
get_python_run_context()

import nltk

from journals2data import data
from journals2data import utils
from journals2data import console

VERBOSE:bool = True

urls = [
    {
        "url": "https://finance.yahoo.com/news/stock-market-news-live-updates-june-14-2021-113039717.html",
        "manual": """
        Stocks narrowly eked out fresh record levels as traders awaited a key monetary policy decision from the Federal Reserve. 

        The S&P 500 pushed into positive territory in the final minutes of trading, logging a fresh record close. The Dow ended lower, while the Nasdaq gained and set its own record closing level. Treasury yields advanced, and the benchmark 10-year yield hovered just below 1.5%. 

        U.S. stocks are hovering at record levels, powered to fresh highs by a combination of rebounding economic activity and corporate profits, and a bevy of ongoing support from both fiscal and monetary policymakers. The duration of this monetary policy support will come into focus this week with the Federal Reserve's policy decision and press conference on Wednesday. With the economy improving from its pandemic-era lows and prices jumping as demand recovers, market participants have been closely monitoring Fed officials' comments to determine when the central bank might start rolling back its crisis-era policies. 

        The Fed has signaled the first course of action would involve easing its asset purchase program, which is currently taking place at a pace of $120 billion per month. The Fed has said it is looking for "substantial further progress" toward its goals of reaching maximum employment and price stability before beginning this roll-back, leaving investors to contemplate what degree of economic improvement might fulfill this prerequisite. Though the U.S. economy has made strides in recovering, the labor market remains more than 7 million jobs short of pre-pandemic levels. And core producer and consumer prices have surged over last year, albeit at elevated levels that will likely not be sustained over the coming months. 

        "Tapering is going to happen over the next few months; the only questions are when, and at what pace," Ian Shepherdson, chief economist for Pantheon Economics, wrote in a note Monday morning. "A month or two either side of the year-end, or a few billion faster or slower tapering, won't make much difference to how the economy performs over the next couple years."

        "The obsession with tapering is a distraction from the real issue, which is whether increased underlying inflation pressure means that the Fed will have to begin raising rates sooner than it currently expects, which is at some point after 2023," he added.

        Meanwhile, as traders await a definitive start to taper talk from the Fed, a number of strategists said they expect similar areas of the market that have outperformed so far this year to continue to do so. With the economy still on the upswing coming out of the pandemic and inflation poised to hold at a level higher than years' past for at least some time, cyclical and value stocks most levered to an economic reopening could remain areas of strength, some said. 

        "I don't think we've seen the exhaustion of that value-cyclical trade. Certainly, we would expect that we're going to see moderation and growth here in the second half of this year from the very heady pace of growth we've had over the last couple of quarters," Mark Luschini, chief investment strategist at Janney Montgomery Scott, told Yahoo Finance. "However, I still think we're going to see well above-trend economic activity, as a consequence of the more uniform reopening of the services industries ... lead to some emergence of inflation that is likely to percolate at an above-trend level over that which we've seen in the last decade or so." 

        —
        4:02 p.m. ET: Stocks end mixed as traders look ahead to Fed decision; Technology shares outperform

        Here were the main moves in markets as of 4:02 p.m. ET:

            S&P 500 (^GSPC): +7.74 (+0.18%) to 4,255.18

            Dow (^DJI): -85.39 (-0.25%) to 34,394.21

            Nasdaq (^IXIC): +104.72 (+0.74%) to 14,174.14

            Crude (CL=F): +$0.11 (+0.16%) to $71.02 a barrel

            Gold (GC=F): -$12.10 (-0.64%) to $1,867.50 per ounce

            10-year Treasury (^TNX): +3.9 bps to yield 1.5010%

        —
        1:05 p.m. ET: Dow trades at session lows 

        The three major indexes were mixed Monday afternoon, with technology stocks outperforming even as Treasury yields advanced and the 10-year yield broke back to 1.5%. The Nasdaq was the only major index in the green. 

        The Dow shed more than 260 points, or 0.8%, at its lowest point in the session Monday afternoon. Walgreens Boots Alliance, Caterpillar and Cisco dragged on the index, while Salesforce and Apple outperformed. The information technology and communication services sectors led in the S&P 500, though sharper declines in materials, financials and industrials kept the index in negative territory.  

        —
        9:45 a.m. ET: 'Bet heavily on every inflation trade' if Fed keeps looking past high prices, hedge fund manager tells CNBC 

        Paul Tudor Jones, billionaire founder and chief investment officer of Tudor Investment Corporation, said investors should lean into asset classes that tend to benefit from higher-inflation environments if the Federal Reserve continues to ignore rising prices and leave monetary policy unchanged, according to an interview with CNBC on Monday.

        "If they treat these numbers — which were material events, they were very material — if they treat them with nonchalance, I think it’s just a green light to bet heavily on every inflation trade,” Jones told CNBC's Squawk Box. Jones added he would "probably buy commodities, buy crypto, buy gold" in this environment. 

        Bitcoin (BTC-USD) prices rallied 13% to top $40,700 following the remarks, as well as after commentary from Tesla CEO Elon Musk that the electric car-maker might resume accepting the cryptocurrency as payment again in the future. Gold (GC=F) extended earlier losses and fell 1.5% to about $1,850 per ounce.

        In April, core personal consumption expenditures (PCE) rose 3.1% over last year, coming in at an almost three-decade high. The Federal Reserve has maintained that these recent inflationary pressures will prove transitory and moderate once the economy laps last year's pandemic-depressed levels. 

        —
        9:30 a.m. ET: Stocks struggle for direction at the open 

        Here's where markets were trading shortly after the opening bell Monday morning: 

            S&P 500 (^GSPC): -1.5 points (-0.04%) to 4,245.94

            Dow (^DJI): -28.2 points (-0.08%) to 34,451.40

            Nasdaq (^IXIC): -0.06 points (-0.00%) to 14,069.36

            Crude (CL=F): +$0.64 (+0.9%) to $71.55 a barrel

            Gold (GC=F): -$28.20 (-1.5%) to $1,851.40 per ounce

            10-year Treasury (^TNX): +0.8 bps to yield 1.47%

        —
        7:28 a.m. ET Monday: Stock futures trade flat 

        Here's where markets were trading Monday morning:

            S&P 500 futures (ES=F): 4,248.00, +2.25 points (+0.05%)

            Dow futures (YM=F): 34,442.00, -20 points (-0.06%)

            Nasdaq futures (NQ=F): 14,040.25, +46 points (+0.33%)

            Crude (CL=F): +$0.40 (+0.56%) to $71.31 a barrel

            Gold (GC=F): -$23.60 (-1.26%) to $1,856.00 per ounce

            10-year Treasury (^TNX): +0.2 bps to yield 1.464%
        """
    },
    {
        "url": "https://www.express.co.uk/life-style/health/1451538/coronavirus-uk-update-vaccine-symptom-sneezing",
        "manual": """
        The coronavirus vaccines deal two decisive blows against COVID-19, both of which are linked. Firstly, they reduce the severity of the disease in people that catch it and this in turn makes the virus less transmissible. However, the vaccines do not stop you from catching COVID-19.

        What's more, people catching COVID-19 post-vaccination have reported a particular symptom not seen in people unvaccinated with the viral disease.

        According to new data published by the ZOE COVID Symptom Study app - the world’s largest ongoing study of COVID-19 - sneezing more than usual can be a sign of COVID-19 but only in people who’ve been vaccinated.

        As the study team explained, sneezing is not normally a symptom of COVID-19, and much more likely to be a sign of a regular cold or allergy.

        "Even though many people with COVID-19 might sneeze, it’s not a definitive symptom because sneezing is so common, especially in the warmer months where people might experience hay fever," the research team said.

        Covid vaccine: Sneezing is a symptom of COVID-19 only seen in people vaccinated (Image: Getty Images)

        However, the study app data shows that people who had been vaccinated and then tested positive for COVID-19 were more likely to report sneezing as a symptom compared with those without a jab.

        This suggests that sneezing a lot with no explanation after you’ve been vaccinated could be a sign of COVID-19.

        "However, it’s important to remember that the link between sneezing and COVID-19 isn’t very strong so you should stay alert to the 20 symptoms of the disease, whether or not you’ve been vaccinated," the app researchers advised.

        Symptoms include:

            High temperature (fever)
            Chills or shivers
            Persistent cough
            Loss or change in smell (anosmia)
            Loss or change in taste (dysgeusia)
            Headache
            Unusual tiredness (fatigue)
            Sore throat
            Sudden confusion (delirium), especially in older people
            Skin rash
            Changes in the mouth or tongue (COVID tongue)
            Red and sore fingers or toes (COVID fingers/toes)
            Shortness of breath
            Chest pains
            Muscle pains
            Hoarse voice
            Diarrhoea
            Skipping meals
            Abdominal pains
            Runny nose.

        How to respond to sneezing post-vaccination

        "If you’ve been vaccinated and start sneezing a lot without an explanation, you should stay home and get a COVID test, especially if you are living or working around people who are at greater risk from the disease," advised the COVID Symptom Study app researchers.

        Right now, you can only get an NHS COVID test if you have a cough, fever or loss of smell.

        But you can get a test through the ZOE COVID Symptom Study if you log any of the known symptoms in the app.

        Sneezing a lot could also be a potential sign that someone vaccinated has COVID-19 and, however mild, should take a test and self-isolate to protect their friends, family and colleagues.

        What to do if you get symptoms again

        According to the NHS, if you get symptoms of coronavirus (COVID-19) again, you must self-isolate immediately and get a PCR test (test that is sent to a lab).

        You should also self-isolate again if:

            Someone you live with gets symptoms
            Someone in your childcare or support bubble gets symptoms and you were in close contact with them since their symptoms started or during the 48 hours before they started.

        The person with symptoms should get a test.

        A support bubble is where someone who lives alone (or just with their children) can meet people from one other household.

        Boris Johnson says coronavirus surge is a 'serious concern'

        According to the NHS, you must self-isolate again even if you've had a positive test result for COVID-19 before.

        "You probably have some immunity to the virus but it's not clear how long it lasts," notes the health body.

        You should also get vaccinated with a coronavirus vaccine if you're eligible.

        COVID-19 vaccines are currently being offered to people aged 18 and over.
        """
    }
]

relative_diffs = []

for element in urls:
    # scrap with n3k
    source = data.Source(
        "",
        "en"
    )
    article = data.Article(
        source,
        element["url"]
    )
    article.scrap()

    # anounce new element
    console.println_ctrl_sequence(
        "****** ****** ****** element[\"url\"] = " + element["url"],
        console.ANSICtrlSequence.PASSED
    )

    # compute score
    if(VERBOSE):
        console.println_debug("****** scraping phase")
    n3k = article.full_text
    if(n3k == None):
        n3k = "error, nothing scraped"
    if(VERBOSE):
        console.println_debug("*** n3k")
        print("\"n3k\": " + n3k)
    manual = element["manual"]
    if(VERBOSE):
        console.println_debug("*** manual")
        print("\"manual\": " + manual)

    #distance calculation
    distance=nltk.edit_distance(n3k , manual)

    console.println_debug("****** distance")
    print("distance = " + str(distance))

    maxlen = max(len(n3k), len(manual))

    console.println_debug("****** maxlen")
    print("maxlen = " + str(maxlen))

    relative_diff = (float(maxlen - distance)/float(maxlen))*100
    relative_diffs.append(relative_diff)

    console.println_debug("****** relative_diff")
    print("score = " + str(relative_diff) + "%")


# general info
console.println_ctrl_sequence(
    "****** ****** ****** general info",
    console.ANSICtrlSequence.PASSED
)

# compute avg relative difference
avg_relative_diff: float = 0
for diff in relative_diffs:
    avg_relative_diff += diff
avg_relative_diff = (
    avg_relative_diff/float(len(relative_diffs))
)
print(
    "Average relative difference: " + 
    str(avg_relative_diff)
)

# get script execution time
execution_time = (time.time() - start_time)
print('Execution time in seconds: ' + str(execution_time))
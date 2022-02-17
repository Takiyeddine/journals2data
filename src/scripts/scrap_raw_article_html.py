# run: onyr@vynae:~/Documents/code/python/journals2data$ python3 src/scripts/scrap_raw_article_html.py 

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup

# run at ".." level
from context import get_python_run_context
get_python_run_context()

from journals2data import utils

brower = None

# objective: create a collection of raw html so as to compare the results on 
# that for every tests


urls = [
    {
        "url": "https://www.wsj.com/articles/novavax-covid-19-vaccine-is-90-effective-in-key-study-11623664800?mod=hp_lead_pos3",
        "manual": """
        An experimental Covid-19 vaccine from Novavax Inc. NVAX 2.07% was 90.4% effective at preventing symptomatic disease in adults in a large clinical trial, the company said, results that move the shot a step closer to global use.

        The 29,960-person study conducted in the U.S. and Mexico also found that the vaccine was similarly effective against newer coronavirus strains, especially the Alpha variant now dominant in the U.S., Novavax said.

        The vaccine, given in two doses three weeks apart, was also generally safe and well tolerated in the study, the company said.

        “Our vaccine works very well even though the virus has mutated significantly,” said Dr. Gregory Glenn, Novavax’s president of research and development.

        Altogether, the results suggest Novavax’s vaccine is on track to become the fourth authorized for use in the U.S. Yet Novavax executives said the regulatory clearances are months away because the company still needs to finish preparing manufacturing.
        Novavax has said it expects more than 2 billion doses of its vaccine will be produced annually when the company and its manufacturing partners reach full capacity.
        Photo: T.J. Kirkpatrick for The Wall Street Journal

        If permitted by regulators, the shot could add a much-needed boost to global efforts to vaccinate people against the coronavirus, which has revealed growing disparities between developed and developing countries.

        Regulatory clearance would infuse a new supply of doses. The company has said it expects more than two billion doses of its vaccine will be produced annually when the company and its manufacturing partners reach full capacity.

        The shots also can be stored at normal refrigerator temperatures, averting the need for the freezers required for some other Covid-19 vaccines.

        Novavax Chief Executive Stanley Erck said the vaccine is likely to become available first in low- to middle-income countries outside the U.S. through the international Covax initiative, possibly by the end of September.

        The company, with manufacturing partners, has pledged to deliver about 1.1 billion doses of the vaccine globally through Covax.
        STAY INFORMED

        “At least in the foreseeable future, we’re going to have a bigger impact” outside the U.S., Mr. Erck said in an interview.

        Novavax, of Gaithersburg, Md., said it plans to request the vaccine’s authorization in the U.S., U.K. and other countries during the third quarter.

        Despite the study results, Novavax said it needs much of that time to ensure that its manufacturing processes meet regulatory standards.

        As more U.S. adults get their Covid-19 vaccines, a variety of side effects are emerging. WSJ’s Daniela Hernandez speaks with an infectious disease specialist on what is common, what isn’t and when to seek medical attention. Photo: Associated Press

        Novavax has experienced various delays in developing and manufacturing its vaccine. In May, the company said shortages in raw materials had caused production delays that would push back targets for reaching peak manufacturing capacity.

        In the U.S., the U.S. Food and Drug Administration plans to take 30 days to review the manufacturing-quality data before Novavax may formally request an authorization of use, Mr. Erck said.

        The company has a contract with the federal government to deliver 110 million doses for use in the U.S. Mr. Erck said the company doesn’t know if the government will decide to distribute them in the U.S. or contribute them to Covax and other countries.

        The vaccine would be the fourth authorized in the U.S., after shots developed by Pfizer Inc. PFE 0.46% with its partner BioNTech SE, BNTX 5.08% Moderna Inc. MRNA 2.34% and Johnson & Johnson. JNJ 0.48%

        The overall efficacy of the Novavax shot in its study approaches the efficacy of at least 94% demonstrated in large trials last year for the Pfizer-BioNTech and Moderna vaccines.

        The Novavax shot’s efficacy is higher than the 66% overall efficacy shown by J&J’s vaccine in a large trial.

        The Pfizer and Moderna trials were conducted before more transmissible variants of the coronavirus spread significantly, while the J&J and Novavax trials were conducted while the variants were spreading.

        Novavax said 82% of the subjects in the study who got symptomatic Covid-19—and for whom genetic-sequence data were available—were infected with newer variants.

        Novavax previously reported positive results from a separate, 15,000-person study of its vaccine in the U.K. There, the vaccine was 89.3% effective at protecting people from Covid-19, including many infected with the Alpha variant of the coronavirus.

        The FDA usually wants to see data from a trial conducted at least partly in the U.S. before deciding whether to authorize a medicine.

        A regulatory go-ahead would be a milestone for Novavax, a small company in the Washington, D.C., suburbs that has never won approval for a vaccine. Novavax shares were down slightly at $209.40 in late-morning trading Monday, after rising in earlier trading.

        Novavax’s vaccine contains proteins resembling the “spike” proteins found on the surface of the coronavirus and are supposed to trigger an immune response to the virus once injected.

        Novavax manufactures the proteins in insect cells.

        The vaccine also contains an adjuvant, a substance designed to enhance immune responses. Novavax’s adjuvant is derived from the bark of an evergreen tree native to Chile.

        This approach of combining a protein with an adjuvant is similar to that of vaccines against other diseases, including GlaxoSmithKline GSK -0.22% PLC’s shingles vaccine, Shingrix.

        It is a different mechanism from the Pfizer-BioNTech and Moderna Covid-19 vaccines, which use gene-based technologies, and those from Johnson & Johnson and AstraZeneca, AZN -0.10% which use viral-vector technology.
        How Novavax's Vaccine Works

        Traditional vaccines use the actual virus to generate an immune response. Novavax's relies on a synthesized version of the coronavirus's outer spike proteins, which are what antibodies use to recognize the virus.

        Scientists make the protein by genetically modifying an unrelated insect virus, a baculovirus, and then using that modified virus to infect cells cloned from the armyworm insect.


        The vaccine is made from a stabilized form of the coronavirus spike protein, which is anchored in a lipid nanoparticle and then injected into the body.

        The purified protein antigens in the vaccine can't replicate and can't cause Covid-19. The vaccine also contains a compound that enhances desired immune system responses to the vaccine.


        Sources: National Institutes of Health, the company

        Novavax started its late-stage, or Phase 3, trial of the Covid-19 vaccine in late December. Federal agencies including the National Institutes of Health provided funding for the trial.

        About two-thirds of the study volunteers received the vaccine in two doses, three weeks apart, while one-third received a placebo.

        Researchers kept track of how many people in each group contracted Covid-19 with symptoms, starting seven days after their second injection.

        The company reported results in a press release, and the data haven’t been vetted by outside experts. Novavax said it plans to submit the results to a peer-reviewed publication.

        Researchers identified 77 cases of mild to severe Covid-19 among all study subjects between January and April. Of these, 14 were among those who had received the vaccine, and 63 among those who had gotten a placebo.

        Novavax said all cases of Covid-19 among vaccinated people in the study were mild, and none met the criteria for moderate and severe, including deaths and hospitalizations.

        By comparison, among the 63 cases in the placebo group, 10 were moderate and four were severe, findings that led Novavax to conclude that the vaccine was 100% effective against moderate and severe Covid-19.

        “The data are terrific,” said Dr. Kathleen Neuzil, professor of vaccinology at the University of Maryland School of Medicine. “This is great news for the world, given the desperate need for more vaccines. It also provides another option in the U.S. if boosters are needed, and for children, as those trials are in progress.”

        The trial coincided with the spread in the U.S. of the Alpha variant of the coronavirus, first identified in the U.K. The highly transmissible strain became the predominant strain circulating in the U.S.

        Novavax sequenced the viruses found in 54 of the 77 cases of symptomatic Covid-19. Of these sequenced cases, 65% were the Alpha strain or other variants of concern, the company said.

        Researchers label a strain as a variant of concern if there is evidence it is more contagious, produces more severe disease or is better able to evade drugs or vaccines.

        Another 17% of the sequenced cases were variants of interest, strains that are generally less prevalent than the variants of concern but which public-health authorities are monitoring.

        Novavax said that the vaccine was 93.2% effective combined against the variants of concern and variants of interest in the study.

        There were only a handful of Covid-19 cases among study subjects caused by certain other variants including those that were first identified in Brazil and India, named gamma and delta, respectively.

        Because the numbers were so small, Novavax wasn’t able to conclude how its vaccine performed against those variants.

        The most common side effects after vaccination, Novavax said, were injection-site pain and tenderness, fatigue, headache and muscle pain. The rates of those side effects were generally higher after the second dose.

        Novavax said the injection site reactions generally lasted less than three days and the other symptoms less than two days. The rate of serious and severe adverse events were low and balanced between the vaccine and placebo groups, the company said.

        One challenge conducting the study, Novavax said, was the availability of authorized vaccines. Study subjects, particularly older adults, who received a placebo began to drop out to get one of the authorized vaccines.

        To stem the tide of dropouts, Novavax in April began to provide its vaccine to those who had received a placebo in the study.

        In all, about 5,000 people dropped out of the study, Novavax said, meaning the Covid-19 cases that were used to determine efficacy occurred among the remaining 25,000 study subjects, Dr. Glenn said.
        """
    },
    {
        "url": "https://eu.usatoday.com/story/news/world/2021/06/14/vladimir-putin-refuses-guarantee-alexei-navalnys-safety-prison/7682827002/",
        "manual": """
        WASHINGTON – Russian President Vladimir Putin said he could not guarantee opposition leader Alexei Navalny would leave prison alive and denied ordering an assassination attempt on the anti-corruption crusader.

        Putin's remarks, made in an interview with NBC News that aired in part on Monday, mark a fresh provocation from the Russian autocrat as he prepares to sit down with U.S. President Joe Biden for a high-stakes summit this week.

        The two leaders will meet June 16 in Geneva, amid escalating tensions over the Kremlin's cyberattacks and election interference in the U.S. and Putin's efforts to stifle dissent inside Russia. 

        Navalny, an activist and one of Putin's fiercest critics, returned to Russia from Germany in January after recovering from poisoning with a nerve agent. He was detained shortly after his arrival in Moscow and sentenced to two years and eight months in prison for violating the terms of his probation while he was treated abroad.

        Navalny initially went on a hunger strike, and his allies say he came close to death before ending his strike on the advice of doctors.

        Asked if he could guarantee Navanly would leave prison alive, Putin claimed he had no say over the matter.

        "Look, such decisions in this country are not made by the president," Putin said.

        Pressed on Navalny's status, Putin said, "He will not be treated any worse than anybody else."

        Biden said on Monday that it would be a "tragedy" if Navalny died in jail. "It would do nothing but hurt his relationships with the rest of the world, in my view, and with me," he said during a news conference in Brussels after meeting with NATO leaders. 

        Navalny's case is likely to be one of many flashpoints between Biden and Putin during Wednesday's meeting.   

        The U.S. intelligence community has determined with "high confidence" that Russia's Federal Security Service used the nerve agent Novichok to poison Navalny last August. The Biden administration imposed sanctions on Russia in the wake of that finding. 

        Putin has denied any involvement in the attack on Navalny, a position he repeated to NBC. 

        "We don't have this kind of habit of assassinating anybody," Putin said when pressed on Navalny's poisoning. 

        The Russian leader also flatly denied that Moscow was behind the recent SolarWinds cyberattack or that the Kremlin interfered in the 2020 presidential election. The Biden administration has sanctioned Russia over both of those matters. 

        "We have been accused of all kinds of things," Putin told NBC. "Election interference, cyberattacks and so on and so forth. And not once, not once, not one time, did they bother to produce any kind of evidence or proof. Just unfounded accusations.

        Tensions are high between US and Russia. Here's what to expect when Biden meets Putin.

        Biden is expected to give Putin a laundry list of grievances. Here are three topics the two leaders will likely discuss at the Geneva summit.

        Putin said the U.S.-Russia relationship has "deteriorated to what is the lowest point in recent years," but said he and Biden would be able to work together on issues of "mutual interest," such as arms control. 

        He shrugged off questions about Biden's affirmative answer, during an interview earlier this year, when he was asked if Putin was a "killer." 

        Biden did not back away from that characterization during Monday's news conference. "When I was asked that question on air, I answered it honestly, Biden said. "I don't think it matters a whole lot in terms of this next meeting we're about to have." 

        A look ahead: With US-Russia relations at low point, Biden, Putin each bring a wariness to Geneva summit

        Putin said he works with people he disagrees with all the time. "People with whom I work ... we argue," the Russia leader said. "We are not bride and groom. We don't swear everlasting love and friendship."

        He did, however, offer warm words for former President Donald Trump, who tried to cultivate close ties with Putin even as his advisers pressed for a tough approach to Russia. 

        "Mr. Trump is an extraordinary individual, talented individual. Otherwise he would not have become U.S. president," Putin said.
        """
    },
    {
        "url": "https://edition.cnn.com/2021/06/14/politics/china-nuclear-reactor-leak-us-monitoring/index.html",
        "manual": """
        (CNN)The US government has spent the past week assessing a report of a leak at a Chinese nuclear power plant, after a French company that part owns and helps operate it warned of an "imminent radiological threat," according to US officials and documents reviewed by CNN.
        The warning included an accusation that the Chinese safety authority was raising the acceptable limits for radiation detection outside the Taishan Nuclear Power Plant in Guangdong province in order to avoid having to shut it down, according to a letter from the French company to the US Department of Energy obtained by CNN.
        Despite the alarming notification from Framatome, the French company, the Biden administration believes the facility is not yet at a "crisis level," one of the sources said.

        While US officials have deemed the situation does not currently pose a severe safety threat to workers at the plant or Chinese public, it is unusual that a foreign company would unilaterally reach out to the American government for help when its Chinese state-owned partner is yet to acknowledge a problem exists. The scenario could put the US in a complicated situation should the leak continue or become more severe without being fixed.

        However, concern was significant enough that the National Security Council held multiple meetings last week as they monitored the situation, including two at the deputy level and another gathering at the assistant secretary level on Friday, which was led by NSC Senior Director for China Laura Rosenberger and Senior Director for Arms Control Mallory Stewart, according to US officials.
        The Biden administration has discussed the situation with the French government and their own experts at the Department of Energy, sources said. The US has also been in contact with the Chinese government, US officials said, though the extent of that contact is unclear.
        The US government declined to explain the assessment but officials at the NSC, State Department and the Department of Energy insisted that if there were any risk to the Chinese public, the US would be required to make it known under current treaties related to nuclear accidents.
        Framatome had reached out to the US in order to obtain a waiver that would allow them to share American technical assistance in order to resolve the issue at the Chinese plant. There are only two reasons why this waiver would be granted, and one is an "imminent radiological threat," the same verbiage used in the June 8 memo.
        The memo claims the Chinese limit was increased to exceed French standards, yet it remains unclear how that compares to US limits.
        "It is not surprising that the French would reach out," according to Cheryl Rofer, a nuclear scientist who retired from Los Alamos National Laboratory in 2001. "In general, this sort of thing is not extraordinary, particularly if they think the country they are contacting has some special ability to help."
        "But China likes to project that everything is just fine, all the time," she added.
        The US could give permission for Framatome to provide the technical assistance or support to help resolve the issue, but it is the Chinese government's decision whether the incident requires shutting down the plant completely, the documents obtained by CNN indicate.
        Ultimately, the June 8 request for assistance from Framatome is the only reason why the US became involved in the situation at all, multiple sources told CNN.
        However, the Taishan Nuclear Power Plant published a statement on its website Sunday night local time, maintaining that environmental readings for both the plant and its surrounding area were "normal."
        The two nuclear reactors in Taishan are both operational, the statement said, adding that Unit 2 had recently completed an "overhaul" and "successfully connected to the grid on June 10, 2021." The statement did not define why or how the plant was overhauled.
        "Since it was put into commercial operation, the Taishan Nuclear Power Plant has strictly controlled the operation of the units in accordance with operating license documents and technical procedures. All operating indicators of the two units have met the requirements of nuclear safety regulations and power plant technical specifications," the statement noted.
        In a separate statement Friday, hours after CNN first reached out for comment, Framatome acknowledged the company "is supporting resolution of a performance issue with the Taishan Nuclear Power Plant in Guangdong Province, China."
        "According to the data available, the plant is operating within the safety parameters. Our team is working with relevant experts to assess the situation and propose solutions to address any potential issue," the statement added.
        Framatome would not directly address the content of the letter to the Department of Energy when asked by CNN.
        The letter comes as tensions between Beijing and Washington remain high and as G7 leaders met this weekend in the United Kingdom with China an important topic of discussion. There are no indications the reports of a leak were discussed at a high level at the summit.
        French utility company Electrictie de France (EDF) said in a statement it has been informed of an increase concentration of "noble gases in the primary circuit" of reactor number one of the Taishan nuclear power plant.
        EDF holds a 30% stake in the company with Chinese state energy company China General Nuclear Power Group in TNPJVC, which owns and operates the power plant in southern China.
        EDF says "the presence of certain noble gases in the primary circuit is a known phenomenon, studied and provided for in the reactor operating procedures," but did not elaborate on gas levels.
        Later on Monday, a spokesperson for EDF said the increased levels of radiation were caused by a "degradation of the housing of the fuel rods."
        The spokesperson affirmed that the levels of radioactivity observed at the plant were below the threshold stipulated by the Chinese authorities, adding that the affected housings are the first of three containment barriers between the rods and the atmosphere.
        The spokesperson noted that the risk of a potential leakage in the rod housing was first discussed following a planned refueling outage in October 2020 after initial measurements led to suspicions of a "lack of tightness" in the housings.
        However, the spokesperson stressed that without a full analysis, it is too early to confirm whether a complete shutdown of the reactor is needed, adding that EDF currently has no information regarding the origin of the rod housing degradation.
        CNN has reached out to the Chinese authorities in Beijing and Guangdong province, where the plant is located, and the Chinese embassy in Washington, DC. None have responded directly, though China is amidst a three-day national holiday that runs through the end of Monday.
        A warning from a French nuclear company
        The issue first emerged when Framatome, a French designer and supplier of nuclear equipment and services that was contracted to help construct and operate the Chinese-French plant, reached out to the US Department of Energy late last month informing them of a potential issue at the Chinese nuclear plant.
        The company, mainly owned by EDF, the French utility company, then submitted an operational safety assistance request on June 3, formally asking for a waiver that would allow them to address an urgent safety matter, to the Department of Energy, warning American officials that the nuclear reactor is leaking fission gas.
        The company followed up with DOE on June 8 asking for an expedited review of their request, according to a memo obtained by CNN.
        "The situation is an imminent radiological threat to the site and to the public and Framatome urgently requests permission to transfer technical data and assistance as may be necessary to return the plant to normal operation," read the June 8 memo from the company's subject matter expert to the Energy Department.
        Framatome reached out to the US government for assistance, the document indicates, because a Chinese government agency was continuing to increase its limits on the amount of gas that could safely be released from the facility without shutting it down, according to the documents reviewed by CNN.
        When asked by CNN for comment, the Energy Department did not directly address the memo's claim that China was raising the limits.
        In the June 8 memo, Framatome informed DOE the Chinese safety authority has continued to raise regulatory "off-site dose limits." It also says the company suspects that limit might be increased again as to keep the leaking reactor running despite safety concerns for the surrounding population.
        "To ensure off-site dose limits are maintained within acceptable bounds to not cause undue harm to the surrounding population, TNPJVC (operator of Taishan-1) is required to comply with an regulatory limit and otherwise shut the reactor down if such a limit is exceeded," the June 8 memo reads.
        It notes that this limit was established at a level consistent with what is dictated by the French safety authority, but "due to the increasing number of failures," China's safety authority, the National Nuclear Safety Administration (NNSA) has since revised the limit to more than double the initial release, "which in turn increases off-site risk to the public and on-site workers."
        As of May 30, the Taishan reactor had reached 90% of the allegedly revised limit, the memo adds, noting concerns the plant operator may be "petitioning the NNSA to further increase the shutdown limit on an exigent basis in an effort to keep running which in turn would continue to increase the risk to the off-site population and the workers at the plant site."
        The NNSA is China's nuclear safety regulatory authority. It oversees the implementation of safety standards at facilities like Taishan.
        The US State Department came into possession of the June 8 letter and immediately began engaging with interagency partners and with the French government, State Department officials said.
        Over the course of 48-72 hours, the US government has been in repeated contact with French officials and US technical experts at DOE, State Department officials said, noting that this flurry of activity was due to the June 8 letter.
        Subsequently, there were several urgent questions for the French government and Framatome, they added. CNN has reached out to the French embassy in Washington for comment.
        Still, Rofer, the retired nuclear scientist, warns that a gas leak could indicate bigger problems.
        "If they do have a gas leak, that indicates some of their containment is broken," Rofer said. "It also argues that maybe some of the fuel elements could be broken, which would be a more serious problem."
        "That would be a reason for shutting down the reactor and would then require the reactor to be refueled," Rofer told CNN, adding that removing the fuel elements must be done carefully.
        For now, US officials do not think the leak is at "crisis level," but acknowledge it is increasing and bears monitoring, the source familiar with the situation told CNN.
        While there is a chance the situation could become a disaster, US officials currently believe it is more likely that it will not become one, the source added.
        China has expanded its use of nuclear energy in recent years, and it represents about 5% of all power generated in the country. According to China Nuclear Energy Association, there were 16 operational nuclear plants with 49 nuclear reactors in China as of March 2021, with the total generation capacity of 51,000 megawatts.
        The Taishan plant is a prestige project built after China signed a nuclear electricity generation agreement with Électricité de France, which is mainly owned by the French government. The construction of the plant started in 2009, and the two units started generating electricity in 2018 and 2019, respectively.

        The city of Taishan has a population of 950,000 and is situated in the southeast of the country in Guangdong province, which is home to 126 million residents and has a GDP of $1.6 trillion, comparable to that of Russia and South Korea.
        CORRECTION: A previous version of this story incorrectly described the National Nuclear Safety Administration (NNSA). It is China's nuclear safety regulatory authority.

        CNN's Kylie Atwood, Kristen Holmes, Yong Xiong and Shanshan Wang contributed to this report.
        """
    },
    {
        "url": "https://www.nasdaq.com/articles/bitcoin-climbs-near-%2440000-after-musk-says-tesla-could-use-it-again-2021-06-14",
        "manual": """
        LONDON/SINGAPORE, June 14 (Reuters) - Bitcoin climbed to shy of $40,000 on Monday, after yet another weekend of price swings following tweets from Tesla boss Elon Musk, who fended off criticism over his market influence and said Tesla sold bitcoin but may resume transactions using it.

        Bitcoin has gyrated to Musk's views for months since Tesla announced a $1.5 billion bitcoin purchase in February and said it would take the cryptocurrency in payment. He later said the electric car maker would not accept bitcoin due to concerns over how mining the currency requires high energy use and contributes to climate change.

        "When there's confirmation of reasonable (~50%) clean energy usage by miners with positive future trend, Tesla will resume allowing Bitcoin transactions," Musk said on Twitter on Sunday.

        Bitcoin BTC=BTSPrallied more than 9% after that message, breaking above its 20-day moving average, and climbed further in Asia to hit $39,838.92.

        "Musk's words caused bitcoin to surge," said Simon Peters, market analyst at eToro.

        It was last up 0.5% at $39,189, straining to escape the relatively tight trading range of this month.

        The market was also supported by software company and major bitcoin-backer MicroStrategy MSTR.O raising half a billion dollars to buy bitcoin, said Bobby Ong, co-founder of crypto analytics website CoinGecko.

        Bitcoin is up about a third this year but has collapsed from a record peak above $60,000 amid a regulatory crackdown in China and Musk's apparently wavering enthusiasm for it. Telsa TSLA.O stock is down about 30% since the company's bitcoin purchase.

        Musk's tweet was made in response to an article based on remarks from Magda Wierzycka, head of cybersecurity firm Syngia SYGJ.J, who in a radio interview last week accused him of "price manipulation" and selling a "big part" of his exposure.

        "This is inaccurate," Musk said. "Tesla only sold ~10% of holdings to confirm BTC could be liquidated easily without moving market."

        Musk had tweeted in May that Tesla "will not be selling any bitcoin" and "has not sold any bitcoin," but investors are keenly awaiting Tesla's next earnings update - due next month - for any disclosure of changes to its position.

        Musk has taken issue with the vast computing power required to process bitcoin transactions and in early June posted messages appearing to lament a breakup with bitcoin.

        (Reporting by Tom Westbrook in Singapore and Tom Wilson in London; Editing by Jacqueline Wong and Chizu Nomiyama)

        The views and opinions expressed herein are the views and opinions of the author and do not necessarily reflect those of Nasdaq, Inc.
        """
    },
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
        "url": "https://www.gamespot.com/articles/ps5-restock-for-gamestop-powerup-rewards-pro-members-at-1130-am-et-today/1100-6493049/",
        "manual": """
        The products discussed here were independently chosen by our editors. GameSpot may get a share of the revenue if you buy anything featured on our site.

        Update: GameStop has notified PowerUp Rewards Pro members that they will be able to purchase a PS5 at 8:30 AM PT / 11:30 AM ET on the GameStop website. If you're a member, check your email for the notification. Be sure you're logged in on the GameStop website ahead of time to take advantage of the early access sale. Supposedly, this is the link where the PS5 will be available.

        This suggests a larger PS5 restock may be available on GameStop's website later today after the early access stock sells out, so even if you're not signed up to GameStop's membership program, keep an eye on the company's Twitter and site.

        GameStop has announced a major new perk coming to its PowerUp Rewards Pro subscription, giving early access to PlayStation 5 and Xbox Series X|S restocks to all members.

        The company first made the announcement via its Instagram and Facebook accounts, the post listing early access among other perks like 10,000 extra reward points and double points on all trade-ins. The post was followed by an email to members with the same information, though with a bit of fine print: new or returning memberships must be activated before Thursday, June 17 at 11:59 PM CST (9:59 PM PT / 12:59 AM ET on June 18). If you sign up before the deadline, make sure to turn on email and Twitter alerts to make sure you're ready for when GameStop announces more details for the early access restock.

        GameStop did not announce any coming restocks on either the PlayStation 5 or Xbox Series X|S with the news, so it is unclear when PowerUp Rewards Pro members will first be able to take advantage of this new perk. GameStop has not restocked PS5s since May 26, while Xbox Series X consoles were available in-store on June 16. However, with the June 17 deadline for signing up to receive the early access, a restock seems imminent.

        The PowerUp Rewards Pro membership costs $20 a year, or $15 a year if you opt for digital Game Informer issues over print. It comes with extra trade credit on games, access to Pro Day sales, a $5 monthly reward certificate, and more.

        The PlayStation 5 and Xbox Series X|S continue to be hot commodities months after their launch. With Amazon's massive Prime Day sale coming soon, check out whether Prime Day PS5 restocks are on their way as well. If you're lucky enough to already have either next-gen console, keep an eye on our list of best Prime Day PlayStation deals and best Prime Day Xbox deals.

            When Is Amazon Prime Day 2021: Dates, Deals, And What To Expect
            Best Early Amazon Prime Day Deals Live Now 2021
            Best Prime Day PlayStation Deals: PS5 And PS4 Deals Available Now
            + Show More Amazon Prime Day 2021 News & Deals Links (4)
            Prime Day Switch Deals: Best Nintendo Switch Discounts So Far
            Best Amazon Prime Day TV Deals 2021: 4K, OLED, And More
            Prime Day Monitor Deals: 1080p, 1440p, And Ultrawide Gaming Monitors
            Prime Day Phone Deals: Samsung Galaxy S21, Google Pixel 3 XL, And More Early Discounts

        """
    },
    {
        "url": "https://www.theguardian.com/world/2021/jun/18/hongkongers-queue-to-buy-apple-daily-copies-after-editor-in-chief-arrested",
        "manual": """
        Hongkongers queued at city news stands before dawn on Friday to buy the latest edition of the Apple Daily newspaper, a day after national security police arrested its editor-in-chief and four other directors.

        On Thursday morning hundreds of officers from the Hong Kong police national security department raided the homes of the employees, including editor-in-chef Ryan Law, and the Apple Daily newsroom for the second time in less than a year. It froze millions of dollars in company assets.

        Police said the raid and arrests were due to alleged breaches of the national security law’s clause against foreign collusion, via more than 30 articles calling for international sanctions against Hong Kong and China. Media and rights groups said authorities were using the law to crackdown on a vocal critic.

        On Friday police announced they had charged two of those arrested with foreign collusion offences, and announced prosecution proceedings against three companies for the same charge. Apple Daily named those charged as editor-in-chief, Law, and CEO Cheung Kim-hung, scheduled to appear in court on Saturday. The others remained in detention pending further investigation.

        The paper’s staff rejected the accusations against them, and vowed to get the paper out regardless, emblazoning the front page with photos of their five arrested bosses, and the headline: “National security police searched Apple, arrested five people, seized 44 news material hard disks.”

        At the bottom of the page, in the yellow colour associated so closely with the pro-democracy movement, the message: “we must press on”.

        The paper increased its print run for Friday more than fivefold to to 500,000.

        Employees had returned to the office only that afternoon, after an hours-long raid by police with an unprecedented warrant allowing the seizure of journalistic materials, Apple Daily said.
        Photographers take photos of copies of Apple Daily coming off the printing press on Friday.
        Photographers take photos of copies of Apple Daily coming off the printing press on Friday. Photograph: Kin Cheung/AP

        They connected keyboards to their phones to type up their stories, live-streamed and surrounded by rival media documenting the process, including printing presses whirring into action. The paper has a usual circulation of about 80,000, but printed half a million in anticipation of people once against buying it in support after a police operation.

        Across the city people bought multiple copies, some handing them out to businesses to give to customers, others Instagramming their haul, including one woman who filled an Ikea bag. The owner of a Mongkok news stand told AFP he normally sells 60 copies of Apple Daily, but on Friday had sold 1,800 before morning.

        Steven Chow, 45, bought three copies of the paper, a controversial and populist tabloid, but which has become a symbol of the pro-democracy movement.

        “There is no perfect media, but it is a unique voice in Hong Kong,” he said. “You may not like it, but I think you need to let them have their voice and survive, it is important.”

        The targeting of Apple Daily marked an escalation in authorities’ attempts to stifle Hong Kong’s media. The city’s security chief, John Lee, warned other journalists on Thursday to “distance” themselves from the accused, who he referred to as “criminals” and “perpetrators” of a conspiracy.

        Lee would neither specify the offending articles or explain how the national security law applied to media – a long running concern since its introduction almost one year ago. Fears now are that any prosecution of the five executives will further strengthen a chilling effect across the industry.

        The police operation was condemned by foreign governments including the US, UK, Australia and the EU, rights organisations and journalism groups. Beijing accused them of vilifying the police and interfering in internal Hong Kong affairs.

        “The facts are clear and the evidence solid, and the cases have nothing to do with press freedom.”

        Rupert Colville, the chief UN human rights spokesperson, said the raid “sends a further chilling message for media freedom.”

        He told Reuters: “We call on Hong Kong authorities to respect their obligations under the International Covenant on Civil and Political Rights, in line with the Basic Law, in particular freedom of expression, freedom of peaceful assembly and association and the right to participate in public affairs.”
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
    },
    {
        "url": "https://www.dailymail.co.uk/news/article-9700729/Double-jabbed-Brits-able-abroad-nearly-170-countries-month.html",
        "manual": """
        Questions are being asked over how Border Force will deal with policing double-jabbed Brits should amber list countries open up. 
        
        British holidaymakers who have received both doses of the Covid-19 vaccine could be given the green light to fly to nearly 170 countries from next month under new government plans. 

        The Home Office has insisted that it has already 'taken steps to reduce wait times for those entering the country' by upgrading e-gates and improving technology. 

        But critics have warned that there could be queues of up to seven hours as flight capacities increase and Border Force officials struggle to check travellers' evidence of vaccination. 
        British tourists at Portgual's Faro Airport as they were forced to interrupt their holidays in the Algarve to return home earlier this month

        British tourists at Portgual's Faro Airport as they were forced to interrupt their holidays in the Algarve to return home earlier this month 

        Those who are fully vaccinated will need provide evidence via the NHS app at border controls and then be able to enjoy trips to amber list nations without having to isolate for 10 days upon returning home.

        Huge numbers of tourists had to scramble home from Portugal earlier this month in order to beat the quarantine deadline when it was dramatically taken off the green list.

        Some 168 destinations are currently on the amber list, including popular holiday spots like Portugal, France, Spain, Italy, Greece and the United States.

        Ministers are still discussing the plans at this early stage, but Boris Johnson could rubber-stamp them in time for millions of lockdown-weary Britons to jump on flights in July.

        The idea would see travellers obliged to take several PCR tests on their return, but if they come back negative, they won't have to remain stuck in their homes like under current rules.

        However it remains to be seen whether the Border Force will be able to cope with such a large number of travellers.

        The under-fire agency was widely criticised over chaotic scenes at Heathrow earlier this year - when travel was heavily-restricted - when passengers had to queue for up to seven hours to get through passport control and at least one passenger collapsed.

        Last month, one Border Force worker told the Guardian that the situation in airports was only set to worsen unless the government were able to ease the workload.  

        'Normally a Brit arriving at passport control would clear immigration in 30 seconds but the current requirements to manually check Covid-19 testing paperwork and quarantine requirements mean that each person is taking 15 minutes to process,' the worker, who wished to stay anonymous, said. 

        'Everyone is back at work– including formally shielding staff – but the truth is that there simply isn't the capacity for staff to carry out the checks demanded by the government.

        'Flights are currently running at around 15% of normal capacity. If they return to anywhere near their normal level, and the processes remain as they are, it's going to be a very frustrating summer of long, four- to six-hour waits,' he said.   

        Footage posted online in April shows a woman lying on the floor of Heathrow Airport being tended to by staff - as many more passengers wait to be cleared through the border

        The video's uploader claims the woman had collapsed following a seven-hour wait for entry clearance

        Footage posted online in April shows a woman lying on the floor of Heathrow Airport being tended to by staff - as many more passengers wait to be cleared through the border
        The agency insisted last week that it has taken steps to reduce wait times for those entering the country, including upgrading e-gates and improving technology at the border

        The agency insisted last week that it has taken steps to reduce wait times for those entering the country, including upgrading e-gates and improving technology at the border

        However, it insisted last week that it has taken steps to reduce wait times for those entering the country, including upgrading e-gates and improving technology at the border. 

        The agency suggested widespread reports of the extent of the delays included 'misleading claims' that they were down to a lack of resource and inadequate staffing levels.

        It claims that improvements to border technology means it has now more than halved the time it takes to check passenger locator forms to two minutes when scanning a passport. It could previously take up to six minutes.

        Border Force also said it had upgraded e-gates at Terminals 2 and 5 at Heathrow and at Gatwick, while there are plans for even more, to speed up processing of passengers returning from green or amber list countries.    

        A Government spokesperson said: 'To protect the public and the UK's vaccine rollout, as international travel resumes the Government will maintain its enhanced borders regime, which include 100% checks and traffic light system for international travel.

        'While we do this, wait times are likely to be longer and we will do all we can to smooth the process, including the roll-out of our e-Gate upgrade programme during the summer and deploying additional Border Force officers.

        'Arrangements for queues and the management of returning passengers are the responsibility of the relevant airport, which we expect to be done in a COVID-secure way.'

        Treasury Secretary Jesse Norman yesterday hinted proposals are in motion, saying: 'We don't want to get left behind by countries which may be adopting a two-jab approach if it can be done safely, carefully and securely.'

        But a Whitehall source has now suggested the scheme is being accelerated, telling the Sun: 'I don't think we can wait for a long time if it is something that we want to do.' 

        The plans are not likely to affect existing rules on red list countries, such as India and Turkey, which require those returning to Britain to quarantine in hotels.

        However, there are concerns about an age divide, with the vast majority of older travellers likely to have received both jabs, while younger holidaymakers may have only received one, or not even that, with 18-and-19-year-olds, for example, only invited to book a first dose this week.  

        'We don't want to see the oldies getting into fights with youths at the airport,' a source said.

        So far, more than 42 million first doses have been administered while more than 30 million have received both jabs. 

        The plans are expected to be ready for discussion by the Cabinet's Covid operations committee ahead of a June 28 deadline by which ministers have pledged to review the traffic light system. 

        Officials are reportedly discussing how the move would affect those who cannot be vaccinated, whether under-18s should be exempt and whether it would apply to Britons or all arrivals.

        Demand for air travel collapsed in March last year when the UK went into lockdown in response to the crisis, with the Government now under pressure to restart international travel by the battered tourism industry.

        Bosses of the travel industry are furious that Portugal, which was originally on the green list, was suddenly put on the amber list within weeks.

        They also believe that the Balearic and Greek Islands should have been included on the green list. The Balearic island, Majorca, for example, currently has a lower Covid rate than the UK.

        It comes as Ryanair and bosses behind three major English airports prepare to take the Government to court over its travel traffic light system, which they say is bringing the industry to its knees.

        The budget airline is set to be joined by Manchester Airports Group (MAG) - the operator of Manchester, East Midlands and Stansted airports - in launching a High Court challenge.

        The legal bid will seek to force the Government to reveal how it decides which countries are placed on the green, amber and red travel lists.

        Outspoken Ryanair chief Michael O'Leary yesterday blasted ministers as 'incompetent' in a scathing attack on the Government's transport policy. 

        Speaking to the Telegraph, who first revealed Ryanair's anticipated legal challenge, Mr O'Leary said: 'I've never come across a more incompetent f****** front bench of ministers. 

        'I have no faith in (Boris) Johnson's government on any of these issues, having completely mismanaged the original lockdowns last year and the reopening now.'

        The Prime Minister's official spokesman insisted during the April disruption that Border Force had the 'right level' of staff despite complaints and chaotic scenes when the unnamed woman appeared unconscious on the floor of UK arrivals. 

        At the time, it was understood only a maximum of 20 of the 40 passport control desks at Heathrow Terminal 2 have been manned because of social distancing.

        Staff have also been in small bubbles because of Covid-19, preventing groups being deployed when the border becomes busy.

        Following the chaos in April, No 10 pushed the blame on passengers, saying people should only travel when 'absolutely necessary' and suggested not enough travellers were filling in their forms correctly or pre-booking tests.

        The Prime Minister's official spokesman said: 'At this stage with where we are on our road map in this global pandemic, people should not be travelling unless absolutely necessary.

        'The Border Force has staff there to check passengers are compliant with our border health measures and we continue to ask that passengers completed the necessary requirements to enter the UK in advance - things like purchasing testing packages'. 

        It was understood at the time the long delays are being caused by a perfect storm of problems with the Home Office, accused of using a 'rigid and inflexible' bubble system for staff.

        This meant those not on the rota for passport control cannot be moved in to ease pressure at peak times, despite social distancing and regular sanitising.

        Huge queues were being made worse because electronic-gates could not be used because the Government was yet to fully digitise the 'passenger locator forms', which travellers must fill in before heading to the UK.

        Unions claimed Heathrow could use all passport control desks if they had installed screens surrounding each booth, rather than the front-facing ones they chose. 

        But they also blamed passengers for failing to fill in the right forms with birder staff they are seeing large numbers of people using fake Covid test certificates that are not properly checked by airlines.
                """
    },
    {
        "url": "https://edition.cnn.com/2021/06/18/middleeast/iran-election-voting-intl/index.html",
        "manual": """
        Tehran, Iran (CNN)Iranians voted Friday in a controversial election that was all but guaranteed to deliver a hardline president after all the other serious contenders were barred from the race.
        The practically uncontested frontrunner is Ebrahim Raisi, the ultra-conservative judiciary chief, who is currently under US sanctions. His only non-conservative election rival is Abdolnaser Hemmati, a former central bank governor running on a moderate platform.
        There were signs on Friday afternoon that election turnout would be lower than hoped for by the country's conservative clerical rulers, as many moderate-minded voters snubbed a poll seen by many as a foregone conclusion. Polls ahead of the election predicted that turnout could be less than 50% for the first time since the establishment of the Islamic Republic in 1979.

        "Each vote counts ... come and vote and choose your president ... this is important for the future of your country," said Supreme Leader Ayatollah Ali Khamenei after casting the first vote early Friday. "Low turnout will increase the pressure of the enemies."

        Raisi emerged as the frontrunner after an election supervisory body known as the Guardian Council barred his main rivals from the race. The move was widely criticized, even by Khamenei, who called some of the disqualifications "unjust."
        Raisi's expected win would come at a pivotal moment for Iran. The next government will have to confront an economic crisis exacerbated by the Covid-19 pandemic and calls for constitutional reform. Tehran is also currently locked in negotiations with the United States about how to revive the 2015 nuclear deal.
        There are also growing questions around the succession plans for the 81-year-old Khamenei. Regardless of who wins the presidential election, under Iran's political system it is the Supreme Leader who makes the final call on all major matters of state. Analysts said victory for Raisi in Friday's presidential election could pave the way for him to become the next Supreme Leader.
        "It's the right of the people to be upset and perhaps some have been upset by the current situation, but I'm asking all of the Iranian people to come to the polls to solve the problems," Raisi tweeted after he cast his ballot on Friday.
        "I hope that people will feel the change soon ... I consider myself a servant for all of the people of Iran," Raisi also said, according to Iran's semi-official Tasnim news agency.
        Iran&#39;s hardline presidential frontrunner could take the country back to a dark past, just as Iranians are itching for change
        Iran's hardline presidential frontrunner could take the country back to a dark past, just as Iranians are itching for change
        Raisi is a close associate of the Supreme Leader with a brutal record on human rights who for decades has played a leading role in the prosecution of political prisoners in Iran.
        In 1988, Raisi was part of a four-person death panel that oversaw the execution of up to 5,000 political prisoners, many of whom were later buried in unmarked graves, according to rights groups.
        Raisi has never commented on the allegations, but it's widely believed that he rarely leaves Iran for fear of retribution or international justice over the executions.
        A few months after Khamenei named Raisi judicial chief in 2019, the US sanctioned him for his role in the 1988 executions and for his involvement in the suppression of the 2009 anti-government Green Movement protests.
        Activists call for boycott
        Polling stations on Friday appeared to be filled largely by conservative voters, many carrying posters of Qasem Soleimani, the top Iranian military commander killed in Baghdad last year on orders from former US President Donald Trump.
        But many Iranians appeared to be staying away from the polls, dismayed by what they see as a heavily engineered election designed to further entrench the power of the country's hardline clerical rulers, despite the public's calls for reforms. Over the last few days, three candidates have dropped out of the race, two of them conservatives who were apparently trying to further boost Raisi's chances.
        On social media, activists called on people to boycott the vote. "I won't be voting. I don't think it's very effective to the situation of the country," said one 22-year-old man before the election. "It's possible that we already know what's going to happen."
        "The government themselves have already selected [the president]. This is the truth," said one disgruntled middle-aged man. "We are in a bad situation. We have to choose only the one they have chosen for us."
        All of the Iranians who criticized the election in interviews with CNN asked not to be named for security reasons.
        On Friday the head of Iran's national security council, Ali Shamkhani, blamed the Trump administration for "disheartening" Iranian voters with its so-called maximum pressure campaign on Tehran. Trump pulled the US out of the nuclear deal with Iran in 2018 and unleashed crushing sanctions on the Iranian economy.
        Fears in the government over voter apathy appeared to spur Khamenei to make a last-minute plea to the electorate on Thursday, warning that poor turnout would play into the hands of Iran's "enemies" and destabilize the country. Previously, Khamenei warned that blank votes would be considered a "sin."
        But in the days leading up to the poll, election posters were sparse, campaign centers were largely empty and the mood was somber.

        "I don't care about elections. Who is meant to take care of us? Rouhani ... Khamenei? They're passing us from one person to another like a basketball," said one woman before the vote who listed a litany of her economic troubles, including being unable to provide the medication needed for her sick son.
        "The worst thing that can happen to me because of my objections is that I'm arrested and killed," she said. "But that's better than watching my son die of sickness." 
        """
    },
    {
        "url": "https://www.nasdaq.com/articles/10-crypto-terms-you-need-to-know-2021-06-18",
        "manual": """
        Once you get a handle on the terminology, it may be easier to understand how cryptocurrency works.

        With so much going on in the world, it's easy to wonder if cryptocurrency feels like too steep a learning curve. A lot of the confusion with crypto is most likely due to the use of words that many of us have never heard.

        Here, we seek to describe some of the most commonly used cryptocurrency terms. That way, if you're starting out and want a foundation upon which to build, you have a basic glossary under your belt.
        1. Address

        An address refers to a specific destination on the network where cryptocurrency is sent. It's like a bank account that holds only cryptocurrency. Each address is used once and is intended to offer a unique, highly-secure place to hold crypto assets.

        Each address consists of a unique set of alphanumeric characters. Once cryptocurrency has been sent from one party to another, the recipient uses that precise set of alphanumeric characters to prove that the cryptocurrency belongs to them and to receive the transaction.
        2. Bitcoin

        Bitcoin is a digital payment system that allows secure peer-to-peer transactions.

        Unlike other payment methods (like Venmo or PayPal) that rely on traditional banking systems, Bitcoin is decentralized. What this means is that any two people located anywhere in the world can exchange digital funds. It also means that each transaction is logged on a blockchain (much like a bank ledger) and distributed across the entire network of cryptocurrency users.

        This distribution protects transactions by making each one transparent. It also cuts out third parties, like banks, companies, and countries. No one controls the Bitcoin network other than the participants. And because it isn't necessary to purchase an entire Bitcoin, anyone can become part of the network by buying a fraction of a coin.
        3. Blockchain

        Rather than being managed centrally (like a central bank that manages U.S. currency), cryptocurrency is managed by a global peer-to-peer network. Blockchain refers to the digital ledger used to store all cryptocurrency transactions. According to Blockgeeks, the best way to understand blockchain is to imagine a spreadsheet that is duplicated thousands of times and sent to a network of different computers. All cryptocurrency transactions that take place are shared and continually reconciled. That means that there is no centralized database that a hacker can corrupt, and all records are public.
        4. Cryptocurrency

        The word cryptocurrency refers to digital or virtual money. It exists solely in electronic form and cannot be carried around like dollar bills or coins. Think of it this way: "crypto" refers to data encryption. "currency" is a medium of exchange (like dollars, pounds, or euros). Like the typical money we're accustomed to, cryptocurrency can be exchanged for goods and services. One primary difference is that cryptocurrency is encrypted to ensure that each transaction is secure. Examples of cryptocurrency include:

            Bitcoin
            Ethereum
            Dogecoin

        5. Fiat

        Fiat currency is government backed but not backed by an asset (like gold). In the U.S., the dollars we carry are fiat currency. Their value is based solely upon our belief that the U.S. government can back them.
        6. Gas

        The gas price is the fee you pay to make a transaction on the blockchain. It covers the cost of paying a "miner" to search out and receive crypto on your behalf. The size of the fee is based on how quickly you want the transaction to be completed.
        7. Mining

        Mining is the process used when new Bitcoins are entered into circulation. This process requires powerful computers that can solve mathematical puzzles and are able to create a new block on the blockchain. It also involves adding safety measures to protect the transaction.
        8. Satoshi Nakamoto

        No one, outside the inventor or inventors, knows who is responsible for inventing Bitcoin. Satoshi Nakamoto is the pseudonym used to refer to the inventor.
        9. Wallet

        A crypto wallet is where all your cryptocurrency coins are stored. The purpose of a wallet is to protect your digital currency. Security is so tight that you lose all access to your cryptocurrency if you ever lose or forget your password. The entire point of cryptocurrency is security without centralization, according to Slate. The only way to provide that security is to make individual users responsible for their passwords.

        There are two main types of crypto wallets -- hot and cold. A hot wallet is connected to the internet. It makes online trades convenient, but is far less secure than a cold wallet. A cold wallet is more like a safe, kept offline in a secure spot that only you can access. It's less convenient than a hot wallet when it comes time to make purchases or trades, but infinitely more secure.
        10. Whale

        The most valuable cryptocurrency addresses are referred to as "whales." A whale is an investor (or group of investors) powerful enough to influence the value of a coin. Let's say a group of whales gets together and decides to sell their Bitcoin at the same time. Naturally, the value of the coins would fall immediately following the mass sell-off. The whales could then take their profits and buy up more coins at a bargain basement price. Anyone can become a whale, although whales are typically large hedge and investment funds.

        Top credit card wipes out interest
        If you have credit card debt, transferring it to this top balance transfer card can allow you to pay 0% interest for a whopping 18 months! That's one reason our experts rate this card as a top pick to help get control of your debt. It'll allow you to pay 0% interest on both balance transfers and new purchases during the promotional period, and you'll pay no annual fee. Read our full review for free and apply in just two minutes. We’re firm believers in the Golden Rule, which is why editorial opinions are ours alone and have not been previously reviewed, approved, or endorsed by included advertisers. The Ascent does not cover all offers on the market. Editorial content from The Ascent is separate from The Motley Fool editorial content and is created by a different analyst team.Dana George has no position in any of the stocks mentioned. The Motley Fool owns shares of and recommends Bitcoin and PayPal Holdings. The Motley Fool recommends the following options: long January 2022 $75 calls on PayPal Holdings. The Motley Fool has a disclosure policy.
        """
    }
]

try:
    # set Firefox headless
    firefox_options = Options()
    firefox_options.headless = True

    brower = webdriver.Firefox(
        options = firefox_options,
        service_log_path="./logs/geckodriver.log"
    )

    # get pages
    for element in urls:
        url = element["url"]

        brower.get(url)
        raw_html: str = brower.page_source

        # filter layer
        raw_html = raw_html.replace("\"", "'") # replace " with '
        manual = element["manual"].replace("\"", "'")

        element["html"] = raw_html
        element["manual"] = manual

    # write to file
    utils.save_json_to_file(urls, "./res/raw_html_articles/articles_clean.json")

finally:
    try:
        brower.close()
    except:
        pass






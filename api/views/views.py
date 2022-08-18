import json
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import requests

from api.models import Country, University

url = 'http://universities.hipolabs.com/search'
university = ('1 December University of Alba Iulia', '42 US', 'Abilene Christian University', 'Adelphi University',
              'Agnes Scott College', 'Aiken Technical College', 'Air Force Institute of Technology',
              'Alabama A&M University',
              'Alabama State University', 'Alamo Colleges', 'Albany State University', 'Albertson College of Idaho',
              'Albion College', 'Alfred University', 'Allegheny College', 'Allentown College of Saint Francis de Sales',
              'Alliant International University', 'Alma College', 'Alverno College', 'Ambassador University',
              'American Coastline University', 'American International College', 'American Public University System',
              'Amherst College', 'Andrews University', 'Angelo State University',
              'Anne Arundel Community College', 'Antioch New England', 'Antioch University',
              'Antioch University - Los Angeles', 'Antioch University - Seattle', 'Appalachian State University',
              'Aquinas College', 'Arcadia College', 'Arizona State University', 'Arizona Western College',
              'Arkansas State University', 'Arkansas Tech University', 'Armstrong State College', 'Ashland University',
              'Assumption College', 'Athens State University', 'Auburn University', 'Auburn University at Montgomery',
              'Augsburg College', 'Augusta University', 'Augustana College (IL)', 'Augustana College (SD)',
              'Aurora University', 'Austin College', 'Austin Community College', 'Austin Peay State University',
              'Averett College', 'Avila College', 'Azusa Pacific University', 'Babson College', 'Baker College',
              'Baker University', 'Baldwin Wallace University', 'Ball State University', 'Baptist Bible College',
              'Bard College', 'Barnard College', 'Barry University', 'Bastyr University', 'Bates College',
              'Baylor College of Medicine', 'Baylor University', 'Bellevue University', 'Belmont University',
              'Beloit College',
              'Bemidji State University', 'Benedictine College', 'Bennington College', 'Bentley College',
              'Berea College',
              'Berklee College of Music', 'Bethany College', 'Bethel College (KS)', 'Bethel University',
              'Brandman University',
              'California Baptist University', 'California Polytechnic State University, Pomona',
              'California Southern University', 'California State University Channel Islands',
              'Career College of Northern Nevada', 'Chabot-Las Positas Community College District',
              'Claremont Graduate University', 'Claremont School of Theology', 'Coastal Alabama Community College',
              'Cold Spring Harbor Laboratory', 'College of Mount Saint Vincent', 'College of Southern Nevada',
              'Colorado Community College System', 'Colorado State University - Global Campus',
              'Columbia Basin College',
              'Columbia College (SC)', 'Columbus State University', 'Contra Costa Community College District',
              'Cégep de Saint-Jérôme', 'DAV Institute of Engineering & Technology',
              'Defense Language Institute Foreign Language Center', 'DigiPen Institute of Technology',
              'ECPI University',
              'Eastern Florida State College', 'Everest College', 'Florida Polytechnic University',
              'Florida State College at Jacksonville', 'Full Sail University', 'Georgia Gwinnett College',
              'Globe University &amp; Minnesota School of Business', 'Grand Canyon University', 'Hallmark University',
              'ITT Technical Institute', 'Icahn School of Medicine at Mount Sinai',
              'Illinois Eastern Community Colleges',
              'Indian River State College', 'International Technological University', 'Keiser University',
              'Keller Graduate School of Management', 'King University', 'Lander University', 'Lasell College',
              'Laurus College', 'Lesley University', 'Lindenwood University', 'Lipscomb University',
              'Los Rios Community College District', 'Lovely Professional University', 'Lynn University',
              'Marine Biological Laboratory', 'Maryville University', 'Marywood University',
              'Mississippi Valley State University', 'Monroe College', 'Morehead State University',
              'Mount St. Mary''s University', 'National Park College', 'New College of Florida',
              'New Jersey City University',
              'North Dakota University System', 'NorthCap University', 'Northwest Florida State College',
              'Oklahoma Christian University', 'Park University', 'Pasco-Hernando State College',
              'Philadelphia College of Osteopathic Medicine', 'Purdue University Northwest',
              'Riverside Community College District', 'Robert Morris University Illinois', 'Roosevelt University',
              'SANS Technology Institute', 'SUNY Maritime College', 'San Diego Christian College',
              'San Mateo County Community College District', 'Seattle Colleges', 'Somaiya Vidyavihar',
              'Southwest Research Institute', 'St. Johns River State College', 'St. Petersburg College',
              'Stevenson University', 'Stratford University', 'Sullivan University', 'The Art Institutes',
              'The College of New Jersey', 'The Principia', 'The Scripps Research Institute', 'Tiffin University',
              'Touro College', 'Trident University', 'Troy University', 'Tusculum College',
              'United States Coast Guard Academy', 'University of Arkansas System eVersity',
              'University of Central Oklahoma',
              'University of Findlay', 'University of Houston-Downtown', 'University of La Verne',
              'University of Mary Washington', 'University of Massachusetts Boston',
              'University of Mississippi Medical Center', 'University of North Georgia',
              'University of Petroleum and Energy Studies', 'University of Pittsburgh Medical Center',
              'University of Texas Rio Grande Valley', 'University of the People', 'Utah Valley Uniersity',
              'Utica College',
              'Valencia College', 'Wagner College', 'Wake Forest Baptist Health', 'Washington &amp; Jefferson College',
              'West Virginia Wesleyan College', 'Western New England University', 'Wilmington University',
              'Wisconsin Lutheran College', 'YTI Career Institute',
              'Yosemite Community College District',
              'Young Harris College', 'Danville Community College')


def crawling_country(self):
    datas = requests.get(url).text
    data = json.loads(datas)
    if Country.objects.count() >= 1:
        raise TypeError("이미 데이터가 존재합니다.")

    for d in data:
        if d.get("name") in university:
            Country.objects.create(
                name=d.get("name", ""),
                code=d.get("alpha_two_code", "")
            )
        else:
            continue
    return JsonResponse({"result": "OK"})


def crawling_university(self):
    datas = requests.get(url).text
    data = json.loads(datas)
    if University.objects.count() >= 1:
        raise TypeError("이미 데이터가 존재합니다.")

    for d in data:
        # import pdb
        # pdb.set_trace()
        if d.get("name") in university:
            University.objects.create(
                country=Country.objects.get(name=d.get("name")),
                webpage=d.get("web_pages", ""),
                name=d.get("name", "")
            )
        else:
            continue

    return JsonResponse({"result": "OK"})

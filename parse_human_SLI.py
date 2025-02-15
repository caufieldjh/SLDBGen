from idg2sl import *
import os

# First download (if needed) and parse the HGNC file with symbol/NCBI Gene/Ensembl mappings
hgnc_fname = SL_DatasetParser.get_local_hgncfile_name()
if not os.path.exists(hgnc_fname):
    SL_DatasetParser.get_hgnc_file()

hgnc = HgncParser(hgnc_fname)
entrez_dict = hgnc.get_entrez_dictionary()
ensembl_dict = hgnc.get_ensembl_dictionary()
synonym_dict = hgnc.get_synonym_dictionary()


def show_stats(name, sli_list):
    pos = sum(sl.is_positive_SLI() for sl in sli_list)
    neg = sum(not sl.is_positive_SLI() for sl in sli_list)
    print("[INFO] %s: %d positive and %d negative entries" % (name, pos, neg))


astsaturov2010 = Astsaturov2010Parser()
astsaturov2010_list = astsaturov2010.parse()
show_stats("Astsaturov et al 2010", astsaturov2010_list)

baldwin2010 = Baldwin2010Parser()
baldwin2010_list = baldwin2010.parse()
show_stats("Baldwin et al 2010", baldwin2010_list)

blomen2015 = Blomen2015Parser()
blomen2015_list = blomen2015.parse()
show_stats("Blomen et al 2015", blomen2015_list)

bommi2008 = Bommi2008Parser()
bommi2008_list = bommi2008.parse()
show_stats("Bommi et al 2008", bommi2008_list)

brough2018 = Brough2018Parser()
brough2018_list = brough2018.parse()
show_stats("Brough et al 2018", brough2018_list)

chakraborty2017 = Chakraborty2017Parser()
chakraborty2017_list = chakraborty2017.parse()
show_stats("chakraborty et al 2017", chakraborty2017_list)

chin2020 = Chin2020Parser()
chin2020_list = chin2020.parse()
show_stats("chin 2020", chin2020_list)

dai2013 = Dai2013Parser()
dai2013_list = dai2013.parse()
show_stats("Dai et al 2013", dai2013_list)

etemadmoghadam2013 = Etemadmoghadam2013Parser()
etemadmoghadam2013_list = etemadmoghadam2013.parse()
show_stats("Etemadmoghadam et al 2013", etemadmoghadam2013_list)

han2017 = Han2017Parser()
han2017_list = han2017.parse()
show_stats("Han et al 2017", han2017_list)

jerby2014 = JerbyArnon2014Parser()
jerby_2014_list = jerby2014.parse()
show_stats("Jerby Arnon et al 2014", jerby_2014_list)

josse2014 = Josse2014Parser()
josse2014_list = josse2014.parse()
show_stats("Josse et al 2014", josse2014_list)

kang2015 = Kang2015Parser()
kang2015_list = kang2015.parse()
show_stats("Kang et al 2015", kang2015_list)

kessler2012 = Kessler2012Parser()
kessler2012_list = kessler2012.parse()
show_stats("Kessler et al 2012", kessler2012_list)

kim2011 = Kim2011Parser()
kim2011_list = kim2011.parse()
show_stats("Kim et al 2011", kim2011_list)

krastev2011 = Krastev2011Parser()
krastev2011_list = krastev2011.parse()
show_stats("Krastev et al 2011", krastev2011_list)

lord2008 = Lord2008Parser()
lord2008_list = lord2008.parse()
show_stats("Lord et al 2008", lord2008_list)

# Luo et al 2009
luo2009parser = Luo2009Parser()
luo2009_list = luo2009parser.parse()
show_stats("Luo et al 2009", luo2009_list)

manual1 = ManualEntry1(entrez=entrez_dict, ensembl=ensembl_dict, synonym=synonym_dict)
manual_list1 = manual1.get_entries()
show_stats("Manually entered single-SLI studies (part zero)", manual_list1)

manual2 = ManualEntry2(entrez=entrez_dict, ensembl=ensembl_dict, synonym=synonym_dict)
manual2_list = manual2.get_entries()
show_stats("Manually entered single-SLI studies (part one)", manual2_list)

manual3 = ManualEntry3(entrez=entrez_dict, ensembl=ensembl_dict, synonym=synonym_dict)
manual3_list = manual3.get_entries()
show_stats("Manually entered (3)", manual3_list)

martin2010 = Martin2010and2011Parser()
martin2010_list = martin2010.parse()
show_stats("Martin et al 2010/2011", martin2010_list)

mengwasser_2019 = Mengwasser2019Parser()
mengwasser_2019_list = mengwasser_2019.parse()
show_stats("Mengwasser et al 2019", mengwasser_2019_list)

mohni2014 = Mohni2014Parser(entrez=entrez_dict, ensembl=ensembl_dict, synonym=synonym_dict)
mohni2014_list = mohni2014.parse()
show_stats("Mohni et al 2014", mohni2014_list)

mondal2019 = Mondal2019Parser()
mondal2019_list = mondal2019.parse()
show_stats("Mondal et al 2019", mondal2019_list)

najm2018 = Najm2018Parser()
najm2018_list = najm2018.parse()
show_stats("Najm et al 2018", najm2018_list)

oser2019 = Oser2019Parser()
oser2019_list = oser2019.parse()
show_stats("Oser et al 2019", oser2019_list)

patidar2020 = Patidar2020Parser()
patidar2020_list = patidar2020.parse()
show_stats("Patidar 2020", patidar2020_list)

schick2019 = Schick2019Parser()
schick2019_list = schick2019.parse()
print("[INFO] Schick et al 2019  n=%d SL interactions" % len(schick2019_list))
show_stats("Schick et al 2019", schick2019_list)

shen2015 = Shen2015Parser()
shen2015_list = shen2015.parse()
show_stats("Shen et al 2015 ", shen2015_list)

shen2017 = Shen2017Parser()
shen2017_list = shen2017.parse()
show_stats("Shen et al 2017", shen2017_list)

srivas2016 = Srivas2016Parser()
srivas2016_list = srivas2016.parse()
show_stats("Srivas et al 2016", srivas2016_list)

steckel2012 = Steckel2012Parser()
steckel2012_list = steckel2012.parse()
show_stats("Steckel et al 2012", steckel2012_list)

sullivan2012 = Sullivan2012Parser()
sullivan2012_list = sullivan2012.parse()
show_stats("Sullivan et al 2012", sullivan2012_list)

sun2019 = Sun2019Parser()
sun2019_list = sun2019.parse()
show_stats("Sun et al 2019", sun2019_list)

toyoshima2008 = Toyoshima2008Parser()
toyoshima2008_list = toyoshima2008.parse()
show_stats("Toyoshima et al 2008", toyoshima2008_list)

turner2008 = Turner2008Parser()
turner2008_list = turner2008.parse()
show_stats("Turner et al 2008", turner2008_list)

vizeacoumar2013 = Vizeacoumar2013Parser()
vizeacoumar2013_list = vizeacoumar2013.parse()
show_stats("Vizeacoumar et al 2013", vizeacoumar2013_list)

wang2016 = Wang2016Parser()
wang2016_list = wang2016.parse()
show_stats("Wang et al 2016", wang2016_list)

wang2017 = Wang2017Parser()
wang2017_list = wang2017.parse()
show_stats("Wang et al 2017", wang2017_list)

wang_2019 = Wang2019Parser()
wang_2019_list = wang_2019.parse()
show_stats("Wang et al 2019", wang_2019_list)

williamson2016 = Williamson2016Parser()
williamson2016_list = williamson2016.parse()
show_stats("Williamson et al 2016", williamson2016_list)

sli_lists = [astsaturov2010_list, baldwin2010_list, bommi2008_list, blomen2015_list, brough2018_list,
             chakraborty2017_list, chin2020_list, dai2013_list, etemadmoghadam2013_list, han2017_list, jerby_2014_list,
             josse2014_list,
             kang2015_list, kessler2012_list, krastev2011_list, lord2008_list, luo2009_list, martin2010_list,
             mengwasser_2019_list, mohni2014_list, mondal2019_list, najm2018_list, oser2019_list, patidar2020_list,
             shen2015_list, shen2017_list, schick2019_list, srivas2016_list, steckel2012_list, sullivan2012_list,
             sun2019_list, toyoshima2008_list, turner2008_list, vizeacoumar2013_list, wang2016_list, wang2017_list,
             wang_2019_list, williamson2016_list, manual_list1, manual2_list, manual3_list]
all_sli_list = []
for l in sli_lists:
    all_sli_list.extend(l)

n = 0
n_SL = 0

output_file = "SL_data.tsv"
fh = open(output_file, 'wt')
fh.write(SyntheticLethalInteraction.get_positives_only_tsv_with_ensembl_header() + "\n")
for sli in all_sli_list:
    n += 1
    if sli.is_positive_SLI():
        fh.write(sli.get_positives_only_tsv_line_with_ensembl(ensembl_dict) + "\n")
        n_SL += 1
fh.close()
print("We got %d interactions including %d synthetic lethal interactions" % (n, n_SL))

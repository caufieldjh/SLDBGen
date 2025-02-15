from idg2sl import SyntheticLethalInteraction
from idg2sl.sl_dataset_parser import SL_DatasetParser
from .sl_constants import SlConstants
import csv


class Vizeacoumar2013Parser(SL_DatasetParser):
    """
    six isogenic cell lines were screened  in parallel using a standardized genome-scale pooled shRNA screening pipeline.
    The HCT116 genetic background was chosen because it is near diploid with intact DNA damage and spindle checkpoints.
    The ‘query' genotypes chosen were PTTG1−/−, BLM−/−, MUS81−/−, PTEN−/− and KRAS+/−
    """

    def __init__(self, fname=None):
        pmid = '24104479'
        super().__init__(fname=fname, pmid=pmid)
        self.sli_list = []
        # old symbols that are assigned to multiple genes
        # Pseudogenes: PMS2L5
        self.unclear_gene_symbols = {'51639', 'PMS2L5'}

    def parseLoF(self, geneA, fname):
        """
        BLM, MUS81, PTEN, PTTG1
        """
        geneAid = self.get_ncbigene_curie(geneA)
        with open(fname) as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter='\t')
            for row in csvreader:
                if not row['Expression'] == 'Expressed':
                    continue
                geneBsym = self.get_current_symbol(row['human gene'])
                if geneBsym in self.entrez_dict:
                    geneB_id = self.get_ncbigene_curie(geneBsym)
                elif geneBsym in self.unclear_gene_symbols:
                    continue
                else:
                    raise ValueError("Could not find iid for %s in Brough 2018 2008 " % geneBsym)
                conf80 = int(row['80% Confidence Interval (P<0.2)'])
                if conf80 == 1:
                    sli = SyntheticLethalInteraction(gene_A_symbol=geneA,
                                                     gene_A_id=geneAid,
                                                     gene_B_symbol=geneBsym,
                                                     gene_B_id=geneB_id,
                                                     gene_A_pert=SlConstants.LOF_MUTATION,
                                                     gene_B_pert=SlConstants.SI_RNA ,
                                                     effect_type='confidence.80%',
                                                     effect_size='true',
                                                     cell_line=SlConstants.HCT_116,
                                                     cellosaurus_id=SlConstants.HCT_116_CELLOSAURUS,
                                                     cancer_type=SlConstants.N_A,
                                                     ncit_id=SlConstants.N_A,
                                                     assay=SlConstants.MULTICOLOR_COMPETITION_ASSAY,
                                                     pmid=self.pmid,
                                                     SL=True)
                    self.sli_list.append(sli)

    def parseKRAS(self):
        """
        BLM is BLM RecQ like helicase
        """
        geneA = 'KRAS'
        geneAid = self.get_ncbigene_curie(geneA)
        fname = 'data/vizeacoumarSuppl4-PTEN.tsv'
        c = 0
        with open(fname) as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter='\t')
            for row in csvreader:
                if not row['Expression'] == 'Expressed':
                    continue
                geneBsym = self.get_current_symbol(row['human gene'])
                if geneBsym in self.entrez_dict:
                    geneB_id = self.get_ncbigene_curie(geneBsym)
                elif geneBsym in self.unclear_gene_symbols:
                    continue
                else:
                    raise ValueError("Could not find iid for %s in Brough 2018 2008 " % geneBsym)
                conf80 = int(row['80% Confidence Interval (P<0.2)'])
                if conf80 == 1:
                    c += 1
                    sli = SyntheticLethalInteraction(gene_A_symbol=geneA,
                                                     gene_A_id=geneAid,
                                                     gene_B_symbol=geneBsym,
                                                     gene_B_id=geneB_id,
                                                     gene_A_pert=SlConstants.ACTIVATING_MUTATION,
                                                     gene_B_pert=SlConstants.SI_RNA,
                                                     effect_type='confidence.80%',
                                                     effect_size='true',
                                                     cell_line=SlConstants.HCT_116,
                                                     cellosaurus_id=SlConstants.HCT_116_CELLOSAURUS,
                                                     cancer_type=SlConstants.N_A,
                                                     ncit_id=SlConstants.N_A,
                                                     assay=SlConstants.MULTICOLOR_COMPETITION_ASSAY,
                                                     pmid=self.pmid,
                                                     SL=True)
                    self.sli_list.append(sli)

    def parse(self):
        blm = 'BLM'
        blm_fname = 'data/vizeacoumarSuppl4-BLM.tsv'
        self.parseLoF(geneA=blm, fname=blm_fname)
        mus81 = 'MUS81'
        mus81_fname = 'data/vizeacoumarSuppl4-MUS81.tsv'
        self.parseLoF(geneA=mus81, fname=mus81_fname)
        pttg1 = 'PTTG1'
        pttg1_fname = 'data/vizeacoumarSuppl4-PTTG1.tsv'
        self.parseLoF(geneA=pttg1, fname=pttg1_fname)
        pten = 'PTEN'
        pten_fname = 'data/vizeacoumarSuppl4-PTEN.tsv'
        self.parseLoF(geneA=pten, fname=pten_fname)
        self.parseKRAS()
        return self.sli_list

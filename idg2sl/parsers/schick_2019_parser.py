from idg2sl import SyntheticLethalInteraction
from idg2sl.sl_dataset_parser import SL_DatasetParser
from .sl_constants import SlConstants


class Schick2019Parser(SL_DatasetParser):
    def __init__(self, fname=None):
        """
        Three synthetic lethal interactions were shown
        SMARCA4-ARID2, SMARCA4-ACTB and SMARCC1-SMARCC2.
        Multiple techniques and cell lines were used
        """
        pmid = "31427792"
        super().__init__(fname=fname, pmid=pmid)

    def get_sli(self, geneA_sym, geneA_id, geneB_sym, geneB_id):
        # Gene A should be eighter NRAS or KRAS.
        # These genes had activating mutations in the cell lines
        sli = SyntheticLethalInteraction(gene_A_symbol=geneA_sym,
                                         species_id="10090",
                                         gene_A_id=geneA_id,
                                         gene_B_symbol=geneB_sym,
                                         gene_B_id=geneB_id,
                                         gene_A_pert=SlConstants.SI_RNA,
                                         gene_B_pert=SlConstants.SI_RNA,
                                         effect_type=SlConstants.N_A,
                                         effect_size=SlConstants.N_A,
                                         cell_line=SlConstants.N_A,
                                         cellosaurus_id=SlConstants.N_A,
                                         cancer_type=SlConstants.N_A,
                                         ncit_id=SlConstants.N_A,
                                         assay=SlConstants.MULTICOLOR_COMPETITION_ASSAY,
                                         pmid=self.pmid,
                                         SL=True)
        return sli

    def parse(self):
        # SMARCA4-ARID2, SMARCA4-ACTB and SMARCC1-SMARCC2.
        smarca4 = "SMARCA4"
        smarca4id = self.get_ncbigene_curie(smarca4)
        arid2 = "ARID2"
        arid2id = self.get_ncbigene_curie(arid2)
        sli_list = []
        sli = self.get_sli(geneA_sym=smarca4, geneA_id=smarca4id, geneB_sym=arid2, geneB_id=arid2id)
        sli_list.append(sli)
        actb = 'ACTB'
        actbid = self.get_ncbigene_curie(actb)
        sli = self.get_sli(geneA_sym=smarca4, geneA_id=smarca4id, geneB_sym=actb, geneB_id=actbid)
        sli_list.append(sli)
        smarcc1 = 'SMARCC1'
        smarcc1_id = self.get_ncbigene_curie(smarcc1)
        smarcc2 = 'SMARCC2'
        smarcc2_id = self.get_ncbigene_curie(smarcc2)
        sli = self.get_sli(geneA_sym=smarcc1, geneA_id=smarcc1_id, geneB_sym=smarcc2, geneB_id=smarcc2_id)
        sli_list.append(sli)
        return sli_list

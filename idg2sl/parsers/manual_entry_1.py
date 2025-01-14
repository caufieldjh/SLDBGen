from idg2sl.parsers.sl_constants import SlConstants
from idg2sl import SyntheticLethalInteraction
from .manual_entry import ManualEntry


class ManualEntry1(ManualEntry):
    """
    In a number of papers, only one or a handful of synthetic lethal interactions are described.
    These are very valuable. It is easiest to enter this information by hand.
    """

    def parse(self):
        pass  # Not implemented. We use other methods from the superclass

    def __init__(self, entrez, ensembl, synonym):
        super().__init__(entrez=entrez, ensembl=ensembl, synonym=synonym)
        self.entries = []
        self._add_reid_2016()
        self._add_parthak_2015()
        self._add_sultana_2013()
        self._add_hoffmann_2014()
        self._add_scholl_2009()
        self._add_barbie_2009()
        self._add_chen_2020()
        self._add_yamada_2020()
        self._add_lelij_2020()
        self._add_liu_2020()
        self._add_huang_2020()
        self._add_szymanska_2020()
        self._add_hu_2020()
        self._add_hu_2020a()
        self._add_villalba_2019()
        self._add_paul_2020()
        self._add_chatterjee2019()
        self._add_parvin_2019()
        self._add_park_2019()
        self._add_van_der_meer_2014()
        self._add_burdova_2019()
        self._add_zhang2019()
        self._add_li2019()
        self._add_sasaki2019()
        self._add_karpelMassler_2017()
        self._add_li_2018()
        self._add_bajrami_2018()
        self._add_jenkins_2018()
        self._add_gong_2019()
        self._add_ding_2019()
        self._add_costa_carbral_2016()
        self._add_sanjiv_2016()
        self._add_wang_2004()
        self._add_sun_2018()
        self._add_pan_2017()
        self._add_ding_2017()
        self._add_kawaguchi_2015()
        self._add_kim_2016()
        self._add_shapiro_2014()
        self._get_noll_2016()
        self._get_sarthy_2007()
        self._add_bukhari_2019()
        self._add_feng_2019()
        self._add_chan_2019()
        self._add_carbajosa_2019()
        self._add_zhu_2010()
        self._add_prahallad_2012()
        self._add_kategaya_2019()

    def _add_kategaya_2019(self):
        """
        Of the diverse DDR genes interrogated by acute RNAi-mediated KD, only MMR gene,
        MLH1, showed SL interaction with WRN.
        """
        pmid = '30898619'
        wrn = 'WRN'
        mlh1 = 'MLH1'
        self.create_and_add_sli(geneA=mlh1, geneB=wrn,
                                geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.HAP1_CELL, cellosaurus=SlConstants.HAP1_CELL,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)
        # There were various negative interactions
        # This synergy was specific to WRN as dual KD of BLM and MLH1 did not exhibit a significant effect on cell proliferation
        blm = 'BLM'
        self.create_and_add_sli(geneA=mlh1, geneB=blm,
                                geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.HAP1_CELL, cellosaurus=SlConstants.HAP1_CELL,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid, sl=False)
        # Dual KD of WRN and the other genes involved in mismatch recognition pathways, MSH2, PMS1, and PMS2,
        # did not phenocopy the synergy observed in WRN and MLH1 dual KD
        sl_neg = {'MSH2', 'PMS1', 'PMS2'}
        for geneB in sl_neg:
            self.create_and_add_sli(geneA=wrn, geneB=geneB,
                                    geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SI_RNA,
                                    cell=SlConstants.HAP1_CELL, cellosaurus=SlConstants.HAP1_CELL,
                                    assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid, sl=False)

    def _add_prahallad_2012(self):
        """
        blockade of the epidermal growth factor receptor (EGFR) shows strong synergy with BRAF(V600E) inhibition.
        We find in multiple BRAF(V600E) mutant colon cancers that inhibition of EGFR by the antibody drug cetuximab or
        the small-molecule drugs gefitinib or erlotinib is strongly synergistic with BRAF(V600E) inhibition, both in
        vitro and in vivo.
        """
        pmid = '22281684'
        egfr = 'EGFR'
        braf = 'BRAF'
        self.create_and_add_sli(geneA=braf, geneB=egfr, geneApert=SlConstants.PHARMACEUTICAL,
                                geneBpert=SlConstants.PHARMACEUTICAL, cancer=SlConstants.COLON_CARCINOMA,
                                ncit=SlConstants.COLON_CARCINOMA_NCIT, assay=SlConstants.PHARAMACEUTICAL_INHIBITION_ASSAY,
                                pmid=pmid)

    def _add_zhu_2010(self):
        pmid = '21031151'
        prkcd = 'PRKCD'  # protein kinase C, delta
        hras = 'HRAS'
        # These are mouse cells but other experiments were done with human cells
        # that document sufficiently the effect
        cell = 'NIH 3T3'
        cellosaurus = 'CVCL_0594'
        mapk8 = 'MAPK8' # current symbol for JNK
        mapk8_id = self.get_ncbigene_curie(mapk8)
        self.create_and_add_sli(geneA=hras, geneB=prkcd, geneApert=SlConstants.ACTIVATING_MUTATION,
                                geneBpert=SlConstants.SH_RNA, cell=cell, cellosaurus=cellosaurus,
                                background_dependency_status=SlConstants.OVEREXPRESSION,
                                background_dependency_gene_symbol=mapk8,
                                background_dependency_gene_id=mapk8_id,
                                assay=SlConstants.APOPTOSIS_ASSAY, pmid=pmid)

    def _add_carbajosa_2019(self):
        pmid = '30890549'
        brca1 = 'BRCA1'
        plk1= 'PLK1'
        self.create_and_add_sli(geneA=brca1, geneB=plk1,
                                geneApert=SlConstants.SH_RNA,
                                geneBpert=SlConstants.SH_RNA,
                                cell=SlConstants.HCT_116, cellosaurus=SlConstants.HCT_116_CELLOSAURUS,
                                assay=SlConstants.PATIENT_DERIVED_XENOGRAFT, pmid=pmid)

    def _add_chan_2019(self):
        """
        WRN is found to have SL with deficient DNA mismatch repair (dMMR) -- but multiple genes contribute to this.
        MMR activity of the MLH1- and MSH3-mutated MSI colorectal cell line HCT116 was restored or not by reintroducing
        these genes or a control chromosome. A rescue was found that was  attributable to MMR restoration as
        CRISPR/Cas9 knock out of  MLH1 re-sensitized HCT116 Ch3+5 to WRN silencing and induced DSB following WRN silencing
        We will therefore curate SL with MLH1

        """
        pmid = '30971823'
        wrn = 'WRN'
        mlh1 = 'MLH1'
        self.create_and_add_sli(geneA=mlh1, geneB=wrn, geneApert=SlConstants.LOF_MUTATION,
                                geneBpert=SlConstants.SH_RNA, cell=SlConstants.HCT_116,
                                cellosaurus=SlConstants.HCT_116_CELLOSAURUS, cancer=SlConstants.COLON_CARCINOMA,
                                ncit=SlConstants.COLON_CARCINOMA_NCIT, assay=SlConstants.CELL_VIABILITY_ASSAY,
                                pmid=pmid)


    def _add_feng_2019(self):
        """
        We  tested the sensitivity of five representative UM cell lines, 92.1, OMM1.3, OMM1.5, Mel270, and Mel202,
        all of which harbor GNAQ mutations, to FAK inhibition using VS-4718, a new generation orally-bioavailable
        FAK inhibitor
        """
        pmid = '30773340'
        gnaq = 'GNAQ'
        ptk2 = 'PTK2'
        self.create_and_add_sli(geneA=gnaq, geneB=ptk2, geneApert=SlConstants.ACTIVATING_MUTATION,
                                geneBpert=SlConstants.PHARMACEUTICAL,cell=SlConstants.MEL270_CELL,
                                cellosaurus=SlConstants.MEL270_CELLOSAURUS,
                                cancer=SlConstants.UVEAL_MELANOMA, ncit=SlConstants.UVEAL_MELANOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_bukhari_2019(self):
        pmid = '30645202'
        wee1 = 'WEE1'
        atr = 'ATR'
        self.create_and_add_sli(geneA=wee1, geneB=atr,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.MDAMB231_CELL, cellosaurus=SlConstants.MDAMB231_CELLOSAURUS,
                                cancer=SlConstants.TRIPLE_NEG_BREAST_CARCINOMA,
                                ncit=SlConstants.TRIPLE_NEG_BREAST_CARCINOMA_NCIT,
                                assay=SlConstants.PHARAMACEUTICAL_INHIBITION_ASSAY, pmid=pmid)

    def _get_min_2017(self):
        pmid = '28138034'
        atr = 'ATR'
        atm = 'ATM'
        self.create_and_add_sli(geneA=atm, geneB=atr, geneApert=SlConstants.PHARMACEUTICAL,
                                geneBpert=SlConstants.DYSFUNCTIONALITY, cell=SlConstants.SNU601_CELL,
                                cellosaurus=SlConstants.SNU601_CELLOSAURUS,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)

    def _get_sarthy_2007(self):
        """
        survivin, CDC2, and C20ORF18 induced differential cell killing in the DLD-1 versus DKS-8 cells.
        C20ORF18 is now RBCK1 (RANBP2-type and C3HC4-type zinc finger containing 1)
        """
        pmid = '17237286'
        kras = 'KRAS'
        birc5 = 'BIRC5'  # gene symbol for survivin
        rbck1 = 'RBCK1'
        gene_b_list = {birc5, rbck1}
        # cannot unambiguously identify CDC2, this symbol is an alias for two current gene symbols
        for geneB in gene_b_list:
            self.create_and_add_sli(geneA=kras, geneB=geneB, geneApert=SlConstants.ACTIVATING_MUTATION,
                                    geneBpert=SlConstants.SI_RNA, cell=SlConstants.DLD1_CELL,
                                    cellosaurus=SlConstants.DLD1_CELLOSAURUS,
                                    cancer=SlConstants.COLON_ADENOCARCINOMA,
                                    ncit=SlConstants.COLON_ADENOCARCINOMA_NCIT,
                                    assay=SlConstants.CELL_VIABILITY_ASSAY,
                                    pmid=pmid)

    def _get_noll_2016(self):
        """
        This stusy ruled out SLIs for two pairs of genes
        """
        pmid = '27375368'
        parg = 'PARG'
        brca1 = 'BRCA1'
        pten = 'PTEN'
        self.create_and_add_sli(geneA=brca1, geneB=parg,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.UWB1_CELL, cellosaurus=SlConstants.UWB1_CELLOSAURUS,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid, sl=False)
        self.create_and_add_sli(geneA=pten, geneB=parg,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.U2OS_CELL, cellosaurus=SlConstants.U2OS_CELLOSAURUS,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid, sl=False)

    def _add_shapiro_2014(self):
        pmid = '24848258'
        ptk2 = 'PTK2'  # (current symbol for FAK, see PMID: 27786412)
        nf2 = 'NF2'  # Merlin
        self.create_and_add_sli(geneA=nf2, geneB=ptk2,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell='malignant pleural mesothelioma cells', cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.PLEURAL_MALIGNANT_MESOTHELIOMA,
                                ncit=SlConstants.PLEURAL_MALIGNANT_MESOTHELIOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)

    def _add_kim_2016(self):
        pmid = '26647789'
        cdkn2a = 'CDKN2A'
        rb1 = 'RB1'
        self.create_and_add_sli(geneA=rb1, geneB=cdkn2a,
                                geneApert=SlConstants.SI_RNA,
                                geneBpert=SlConstants.LOF_MUTATION,
                                cell=SlConstants.H82_CELL, cellosaurus=SlConstants.H82_CELLOSAURUS,
                                cancer=SlConstants.NON_SMALL_CELL_LUNG, ncit=SlConstants.NON_SMALL_CELL_LUNG_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)

    def _add_kawaguchi_2015(self):
        """
        We thus treated CD26 knockdown cells with ABT-737, a Bcl-xL/-2/-w inhibitor, and observed that the synthetic
         lethal interaction of combined Bcl-xL and CD26 inhibition induced significant apoptosis and impaired cellular viability.
        """
        pmid = '25297967'
        bcl2l1 = 'BCL2L1'  # was Bcl-xL
        dpp4 = 'DPP4'  # was CD26
        # Huh-7 (CVCL_0336)
        self.create_and_add_sli(geneA=bcl2l1, geneB=dpp4,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.HUH7_CELL, cellosaurus=SlConstants.HUH7_CELLOSAURUS,
                                cancer=SlConstants.HEPATOCELLULAR_CARCINOMA,
                                ncit=SlConstants.HEPATOCELLULAR_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)

    def _add_ding_2017(self):
        pmid = '30323337'
        TALDO1 = 'TALDO1'
        ERBB2 = 'ERBB2'  # current symbol for HER-2
        self.create_and_add_sli(geneA=ERBB2, geneB=TALDO1,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.CRISPR_CAS9,
                                cell=SlConstants.MDAMB361_CELL, cellosaurus=SlConstants.MDAMB361_CELLOSUARUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.SG_RNA_DEPLETION_ASSAY, pmid=pmid)
        igf1r = 'IGF1R'
        self.create_and_add_sli(geneA=ERBB2, geneB=igf1r,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.CRISPR_CAS9,
                                cell=SlConstants.MDAMB361_CELL, cellosaurus=SlConstants.MDAMB361_CELLOSUARUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.SG_RNA_DEPLETION_ASSAY, pmid=pmid)

    def _add_pan_2017(self):
        """
        concomitant p53 activation and Bcl-2 inhibition overcome apoptosis resistance and markedly prolong survival in
        three mouse models of resistant acute myeloid leukemia (AML). Combining the p53 activator RG with ABT at a 5:1
        or 1:1 ratio augmented apoptosis and reduced live cell numbers to a significantly greater extent than either
        agent alone
        """
        pmid = '29232553'
        tp53 = 'TP53'
        bcl2 = 'BCL2'  # correct symbol for BCL-2
        self.create_and_add_sli(geneA=tp53, geneB=bcl2, geneApert=SlConstants.AGONIST,
                                geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.MOLM13_CELL, cellosaurus=SlConstants.MOLM13_CELLOSAURUS,
                                cancer=SlConstants.ADULT_AML, ncit=SlConstants.ADULT_AML_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)

    def _add_sun_2018(self):
        """
        BRD4i markedly and consistently decreased CtIP, part of the MRN complex that commits cells to DSB repair.
        BRD4i extensively rewired protein networks, including multiple components of the DNA damage response pathway
        """
        pmid = '29533782'
        BRD4 = 'BRD4'
        parp1 = 'PARP1'
        self.create_and_add_sli(geneA=parp1, geneB=BRD4,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.N_A, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY,
                                pmid=pmid)


    def _add_wang_2004(self):
        pmid = '15144957'
        myc = 'MYC'
        TNFRSF10B = 'TNFRSF10B'  # current symbol for DR5
        self.create_and_add_sli(geneA=myc, geneB=TNFRSF10B,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.AGONIST,
                                cell=SlConstants.IMR90_CELL, cellosaurus=SlConstants.IMR90_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_sanjiv_2016(self):
        """
        CHK1 now known as CHEK1
        """
        pmid = '26748709'
        atr = 'ATR'
        check1 = 'CHEK1'
        self.create_and_add_sli(geneA=atr, geneB=check1,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.U2OS_CELL, cellosaurus=SlConstants.U2OS_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_costa_carbral_2016(self):
        pmid = '26881434'
        kras = 'KRAS'
        cdk1 = 'CDK1'
        self.create_and_add_sli(geneA=kras, geneB=cdk1,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.LIM1215_CELL, cellosaurus=SlConstants.LIM1215_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_ding_2019(self):
        """
        The current symbol for BRG1 is SMARCA4
        """
        pmid = '30496141'
        pten = 'PTEN'
        smarca4 = 'SMARCA4'
        self.create_and_add_sli(geneA=pten, geneB=smarca4,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.LNCAP_CELL, cellosaurus=SlConstants.LNCAP_CELLOSAURUS,
                                cancer=SlConstants.PROSTATE_CARCINOMA, ncit=SlConstants.PROSTATE_CARCINOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_van_der_meer_2014(self):
        pmid = '24771642'
        pim1 = 'PIM1'
        plk1 = 'PLK1'
        self.create_and_add_sli(geneA=pim1, geneB=plk1,
                                geneApert=SlConstants.OVEREXPRESSION, geneBpert=SlConstants.SH_RNA,
                                cell=SlConstants.LNCAP_CELL, cellosaurus=SlConstants.LNCAP_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.PATIENT_DERIVED_XENOGRAFT, pmid=pmid)


    def _add_gong_2019(self):
        aurka = 'AURKA'
        rb1 = 'RB1'
        pmid = '30373917'
        self.create_and_add_sli(geneA=rb1, geneB=aurka,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell='RB1-Mutant Cancer Cells', cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_jenkins_2018(self):
        tnk2 = 'TNK2'
        ptpn11 = 'PTPN11'
        pmid = '30018082'
        self.create_and_add_sli(geneA=ptpn11, geneB=tnk2,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.N_A, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.JMML, ncit=SlConstants.JMML_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_bajrami_2018(self):
        """
        The cell adhesion glycoprotein E-cadherin (CDH1) is commonly inactivated in breast tumors.
        In order to identify E-cadherin synthetic lethal effects from our MCF7 isogenic cell line siRNA screen,
        we calculated the difference in siRNA Z scores between E-cadherin defective and E-cadherin proficient cells
        and identified 104 E-cadherin synthetic lethal effects (p < 0.05, Fig. 1E; Supplementary Table S3).
        The authors go on to validate ROS1 in detail and do not further analyze these candidates.
        The supplement 3 is an image that cannot easily be ingested -- therefore, we ingest only this highly
        validated SL interaction.
        """
        cdh1 = 'CDH1'
        ros1 = 'ROS1'
        pmid = '29610289'
        self.create_and_add_sli(geneA=cdh1, geneB=ros1,
                                geneApert=SlConstants.CRISPR_CAS9, geneBpert=SlConstants.SI_RNA,
                                cell=SlConstants.MCF7_CELL, cellosaurus=SlConstants.MCF7_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_li_2018(self):
        atm = 'ATM'
        pten = 'PTEN'
        pmid = '29522753'
        self.create_and_add_sli(geneA=pten, geneB=atm,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.MDAMB468_CELL, cellosaurus=SlConstants.MDAMB468_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_karpelMassler_2017(self):
        """
        bcl-xL is BCL2L1
        """
        bcl2l1 = 'BCL2L1'
        idh1 = 'IDH1'
        pmid = '29057925'
        self.create_and_add_sli(geneA=idh1, geneB=bcl2l1,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                cell=SlConstants.T98G_CELL, cellosaurus=SlConstants.T98G_CELLOSAURUS,
                                cancer=SlConstants.GLIOBLASTOMA, ncit=SlConstants.GLIOBLASTOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_sasaki2019(self):
        parg = 'PARG'
        dusp22 = 'DUSP22'
        pmid = '31142510'
        self.create_and_add_sli(geneA=parg, geneB=dusp22,
                                geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SH_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.A549_CELL, cellosaurus=SlConstants.A549_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.SH_RNA, pmid=pmid)


    def _add_li2019(self):
        """
        Note CBP is now called CREBBP
        p300 is now EP300
        """
        crebbp = 'CREBBP'
        ep300 = 'EP300'
        pmid = '31223286'
        self.create_and_add_sli(geneA=crebbp, geneB=ep300,
                                geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.CELL_5637, cellosaurus=SlConstants.CELL_5637_CELLOSAURUS,
                                cancer=SlConstants.BLADDER_CARCINOMA, ncit=SlConstants.BLADDER_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_zhang2019(self):
        """
        double inhibition of Aur-A and mTOR showed significant synergistic effects in TNBC cell lines and a xenograft model,
        """
        mtor = 'MTOR'
        aurka = 'AURKA'
        pmid = '31406104'
        self.create_and_add_sli(geneA=mtor, geneB=aurka,
                                geneApert=SlConstants.PHARMACEUTICAL,
                                geneBpert=SlConstants.PHARMACEUTICAL,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell='TNBC cell lines', cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.TRIPLE_NEG_BREAST_CARCINOMA,
                                ncit=SlConstants.TRIPLE_NEG_BREAST_CARCINOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_burdova_2019(self):
        ccnf = 'CCNF'  # cyclin F
        chek1 = 'CHEK1'  # the authors use chk1
        pmid = '31424118'
        self.create_and_add_sli(geneA=chek1, geneB=ccnf,
                                geneApert=SlConstants.PHARMACEUTICAL,
                                geneBpert=SlConstants.CRISPR_CAS9,
                                effecttype=SlConstants.N_A,
                                effectsize=SlConstants.N_A,
                                cell='cyclin F knock-out cell line', cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_park_2019(self):
        myc = 'MYC'
        aurka = 'AURKA'
        pmid = '31429028'
        self.create_and_add_sli(geneA=myc, geneB=aurka,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell='Myc-overexpressing lymphoma cell lines', cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.PATIENT_DERIVED_XENOGRAFT, pmid=pmid)


    def _add_parvin_2019(self):
        lmo2 = 'LMO2'
        parp1 = 'PARP1'
        pmid = '31447348'
        self.create_and_add_sli(geneA=lmo2, geneB=parp1,
                                geneApert=SlConstants.OVEREXPRESSION, geneBpert=SlConstants.PHARMACEUTICAL,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.DOHH2_CELL, cellosaurus=SlConstants.DOHH2_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_chatterjee2019(self):
        pten = 'PTEN'
        pdk1 = 'PDK1'  # Note the authors use the wrong symbol ('PDHK1') for pyruvate dehydrogenase kinase 1
        pmid = '31461649'
        self.create_and_add_sli(geneA=pten, geneB=pdk1,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SH_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.N_A, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_reid_2016(self):
        """
         PLK1 NCBI Gene id 5347 and CKS1B NCBI Gene id 1163 
         """
        pmid = '27558135'
        cell_line = 'multiple.breast.cancer.cell.lines'
        self.create_and_add_sli(geneA='PLK1', geneB="CKS1B",
                                geneApert=SlConstants.SH_RNA, geneBpert=SlConstants.OVEREXPRESSION,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=cell_line, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.BREAST_CARCINOMA, ncit=SlConstants.BREAST_CARCINOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY,
                                pmid=pmid)


    def _add_parthak_2015(self):
        """
        # just 2 SL Interactions, hardcoded
        # SRC Gene is proto-oncogene blocked by Dasatinib
        # trying to maximise the Dasatinib sensitivity by SL interaction
        """
        src = 'SRC'
        csnk2a1 = "CSNK2A1"
        pmid = '26437225'
        effect_type = "correlation"
        self.create_and_add_sli(geneA=src, geneB=csnk2a1,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.COHORT_STUDY,
                                effecttype=effect_type, effectsize='-0.82',
                                cell=SlConstants.N_A, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.RECURRENT_OVARIAN_CANCER,
                                ncit=SlConstants.RECURRENT_OVARIAN_CANCER_NCIT,
                                assay=SlConstants.PHARAMACEUTICAL_INHIBITION_ASSAY, pmid=pmid)

        prkce = "PRKCE"
        self.create_and_add_sli(geneA=src, geneB=prkce,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.COHORT_STUDY,
                                effecttype=effect_type, effectsize='-0.96',
                                cell=SlConstants.N_A, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.RECURRENT_OVARIAN_CANCER,
                                ncit=SlConstants.RECURRENT_OVARIAN_CANCER_NCIT,
                                assay=SlConstants.PHARAMACEUTICAL_INHIBITION_ASSAY, pmid=pmid)


    def _add_sultana_2013(self):
        atr = 'ATR'
        xrcc1 = 'XRCC1'
        pmid = '23451157'
        self.create_and_add_sli(geneA=atr, geneB=xrcc1,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.OVCAR3_CELL, cellosaurus=SlConstants.OVCAR3_CELLOSAURUS,
                                cancer=SlConstants.OVARIAN_SEROUS_ADENOCARCINOMA,
                                ncit=SlConstants.OVARIAN_SEROUS_ADENOCARCINOMA_NCIT,
                                assay=SlConstants.CISPLATIN_CYTOTOXICITY_ASSAY, pmid=pmid)


    def _add_hoffmann_2014(self):
        """
        BRG1 and BRM identified as a SL pair in various different cancer cells
        BRM and BRG1 are closely related paralogs that function as mutually exclusive ATP-dependent catalytic subunits
        of the mSWI/SNF complexes, including A-549 (CVCL_0023)
        The current symbol for BRM is SMARCA2
        The current symbol for BRG1 is SMARCA4

        """
        smarca2 = 'SMARCA2'
        smarca2_perturbation = SlConstants.SI_RNA
        smarca4 = 'SMARCA4'
        smarca4_perturbation = SlConstants.LOF_MUTATION
        pmid = '24520176'
        self.create_and_add_sli(geneA=smarca2, geneB=smarca4,
                                geneApert=smarca2_perturbation, geneBpert=smarca4_perturbation,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.A549_CELL, cellosaurus=SlConstants.A549_CELLOSAURUS,
                                cancer=SlConstants.LUNG_ADENOCARCINOMA, ncit=SlConstants.LUNG_ADENOCARCINOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_barbie_2009(self):
        """
        Paper is about one SLI
        """
        kras = 'KRAS'
        tbk1 = 'TBK1'
        pmid = '19847166'
        self.create_and_add_sli(geneA=kras, geneB=tbk1,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.N_A, cellosaurus=SlConstants.N_A,
                                assay=SlConstants.RNA_INTERFERENCE_ASSAY,
                                cancer=SlConstants.LUNG_ADENOCARCINOMA, ncit=SlConstants.LUNG_ADENOCARCINOMA_NCIT,
                                pmid=pmid)


    def _add_scholl_2009(self):
        """
        KRAS and  STK33
        Scholl C et al. Synthetic lethal interaction between oncogenic KRAS dependency and
        STK33 suppression in human cancer cells. Cell. 2009;137(5):821-834.
        """
        kras = 'KRAS'
        stk33 = 'STK33'
        pmid = '19490892'
        self.create_and_add_sli(geneA=kras, geneB=stk33,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.HCT_116, cellosaurus=SlConstants.HCT_116_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_chen_2020(self):
        pten = 'PTEN'
        mcl1 = 'MCL1'
        pmid = '32737157'
        cell_line = 'isogeneic GBM cell lines'
        self.create_and_add_sli(geneA=pten, geneB=mcl1,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=cell_line, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.PHARAMACEUTICAL_INHIBITION_ASSAY, pmid=pmid)


    def _add_yamada_2020(self):
        arid1a = 'ARID1A'
        ezh2 = 'EZH2'
        pmid = '32506298'
        cell_line = 'isogeneic GBM cell lines'
        self.create_and_add_sli(geneA=arid1a, geneB=ezh2,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.PHARMACEUTICAL,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=cell_line, cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.GASTRIC_CARCINOMA, ncit=SlConstants.GASTRIC_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_lelij_2020(self):
        stag1 = 'STAG1'
        stag2 = 'STAG2'
        pmid = '32467316'
        self.create_and_add_sli(geneA=stag1, geneB=stag2,
                                geneApert=SlConstants.CRISPR_CAS9, geneBpert=SlConstants.LOF_MUTATION,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.KBM7_CELL, cellosaurus=SlConstants.KBM7_CELLOSAURUS,
                                cancer=SlConstants.CML_BCRABL_POS, ncit=SlConstants.CML_BCRABL_POS_NCIT,
                                assay=SlConstants.CRISPR_CAS9_INTERFERENCE_ASSAY, pmid=pmid)


    def _add_liu_2020(self):
        """
        Silencing p300 or CBP selectively inhibited the viability of PTEN-/- HCT116 cells, but not PTEN+/+ ones,
        indicating that the inhibition of p300 and CBP was likely to mediate the synthetic lethality phenotype induced
        by AA
        """
        pten = 'PTEN'
        ep300 = 'EP300'
        pmid = "32398948"
        self.create_and_add_sli(geneA=pten, geneB=ep300,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.HCT_116, cellosaurus=SlConstants.HCT_116_CELLOSAURUS,
                                cancer=SlConstants.COLON_CARCINOMA, ncit=SlConstants.COLON_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)

        crebbp = 'CREBBP'
        self.create_and_add_sli(geneA=crebbp, geneB=ep300,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.HCT_116, cellosaurus=SlConstants.HCT_116_CELLOSAURUS,
                                cancer=SlConstants.COLON_CARCINOMA, ncit=SlConstants.COLON_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_huang_2020(self):
        ezh2 = 'EZH2'
        pbrm1 = 'PBRM1'
        pmid = '32093567'
        self.create_and_add_sli(geneA=ezh2, geneB=pbrm1,
                                geneApert=SlConstants.PHARMACEUTICAL, geneBpert=SlConstants.LOF_MUTATION,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.A704_CELL, cellosaurus=SlConstants.A704_CELLOSAURUS,
                                cancer=SlConstants.RENAL_CELL_CARCINOMA,
                                ncit=SlConstants.RENAL_CELL_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_szymanska_2020(self):
        vps4a = 'VPS4A'
        vps4b = 'VPS4B'
        pmid = '31930723'
        self.create_and_add_sli(geneA=vps4a, geneB=vps4b,
                                geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.HCT_116, cellosaurus=SlConstants.HCT_116_CELLOSAURUS,
                                cancer=SlConstants.COLON_CARCINOMA, ncit=SlConstants.COLON_CARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY,
                                pmid=pmid)


    def _add_hu_2020(self):
        kras = 'KRAS'
        SLC7A11 = 'SLC7A11'
        pmid = '31874110'
        self.create_and_add_sli(geneA=kras, geneB=SLC7A11,
                                geneApert=SlConstants.ACTIVATING_MUTATION, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell='KRAS isogenic cell lines', cellosaurus=SlConstants.N_A,
                                cancer=SlConstants.LUNG_ADENOCARCINOMA, ncit=SlConstants.LUNG_ADENOCARCINOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_hu_2020a(self):
        tbk1 = 'TBK1'
        vhl = 'VHL'
        pmid = '31810986'
        self.create_and_add_sli(geneA=vhl, geneB=tbk1,
                                geneApert=SlConstants.LOF_MUTATION, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.UMRC6_CELL, cellosaurus=SlConstants.UMRC6_CELLOSAURUS,
                                cancer=SlConstants.RENAL_CELL_CARCINOMA,
                                ncit=SlConstants.RENAL_CELL_CARCINOMA_NCIT,
                                assay=SlConstants.GROWTH_INHIBITION_ASSAY, pmid=pmid)


    def _add_villalba_2019(self):
        tmprss4 = 'TMPRSS4'
        ddr1 = 'DDR1'
        pmid = '31659178'
        self.create_and_add_sli(geneA=tmprss4,
                                geneB=ddr1,
                                geneApert=SlConstants.SI_RNA,
                                geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.H358_CELL, cellosaurus=SlConstants.H358_CELLOSAURUS,
                                cancer=SlConstants.MINIMALLY_INVASIVE_LUNG_ADENOCARCINOMA,
                                ncit=SlConstants.MINIMALLY_INVASIVE_LUNG_ADENOCARCINOMA_NCIT,
                                assay=SlConstants.CELL_VIABILITY_ASSAY, pmid=pmid)


    def _add_paul_2020(self):
        """
        G - Quadruplex - Binding  Small Molecule Induces  Synthetic  Lethality in Breast
        Cancer Cells by Inhibiting c - MYC and BCL2 Expression
        """
        myc = "MYC"
        bcl2 = "BCL2"
        pmid = "31621996"
        self.create_and_add_sli(geneA=myc, geneB=bcl2,
                                geneApert=SlConstants.SI_RNA, geneBpert=SlConstants.SI_RNA,
                                effecttype=SlConstants.N_A, effectsize=SlConstants.N_A,
                                cell=SlConstants.MCF7_CELL, cellosaurus=SlConstants.MCF7_CELLOSAURUS,
                                cancer=SlConstants.N_A, ncit=SlConstants.N_A,
                                assay=SlConstants.CYTOTOXICITY_ASSAY, pmid=pmid)

    def get_entries(self):
        return self.entries

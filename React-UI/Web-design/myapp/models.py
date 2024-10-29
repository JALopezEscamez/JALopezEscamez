from django.db import models

class GeneBcells(models.Model):
    id = models.AutoField(primary_key=True),
    gene_name = models.CharField(unique= True, max_length= 255, blank=True, null=True)
    avg_log2fc_1 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_1 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    avg_log2fc_2 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_2 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    avg_log2fc_3 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_3 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    avg_log2fc_4 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_4 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    avg_log2fc_5 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_5 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    avg_log2fc_6 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_6 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    avg_log2fc_7 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)
    p_val_adj_7 = models.DecimalField(max_digits=10, decimal_places= 6,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gene_bcells'

class GeneCD4(models.Model):
    gene_id = models.AutoField(primary_key=True),
    gene_name = models.CharField(unique= True, max_length= 255, blank=True, null=True)
    avg_log2fc_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)

    class Meta:
        managed = False
        db_table = 'gene_cd4'


class GeneCD8(models.Model):
    gene_id = models.AutoField(primary_key=True),
    gene_name = models.CharField(unique= True, max_length= 255, blank=True, null=True)
    avg_log2fc_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)

    class Meta:
        managed = False
        db_table = 'gene_cd8'


class GeneMonocytes(models.Model):
    gene_id = models.AutoField(primary_key=True),
    gene_name = models.CharField(unique= True, max_length= 255, blank=True, null=True)
    avg_log2fc_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)

    class Meta:
        managed = False
        db_table = 'gene_monocytes'


class GeneNkcells(models.Model):
    gene_id = models.AutoField(primary_key=True),
    gene_name = models.CharField(unique= True, max_length= 255, blank=True, null=True)
    avg_log2fc_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_1 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_2 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_3 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_4 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_5 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_6 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)
    avg_log2fc_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null=True)
    p_val_adj_7 = models.DecimalField(max_digits=200, decimal_places= 200,blank=True, null = True)

    class Meta:
        managed = False
        db_table = 'gene_nkcells'


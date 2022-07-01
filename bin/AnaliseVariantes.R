tableVariantes = as.data.frame(read.csv("/home/fabio/projetos-doutorado/analise-gnomad/data/dadosGnomAD/variantesGeneVGnomad-RefGeneCode-QtdeGenomaExoma.csv", sep=";", dec=",", header = TRUE))
nrow(tableVariantes)

tableExoma=subset(tableVariantes, tableVariantes$Source='E')


exoma = subset(tableVariantes, tableVariantes$Source=='E', drop = TRUE)
nrow(exoma)

genoma = subset(tableVariantes, Source == 'EG', drop = TRUE)
nrow(genoma)



 

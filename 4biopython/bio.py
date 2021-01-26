from Bio.Seq import Seq
from Bio import SeqIO

# Sequencia Complementar

minha_primeira_sequencia = Seq("ATG")

print(minha_primeira_sequencia)

seq_complementar = minha_primeira_sequencia.complement()

print(seq_complementar)

# Sequencia Reversa Complementar

seq_complementar_reversa = minha_primeira_sequencia.complement()
print(seq_complementar_reversa)


# Transcrição

seq_rna = minha_primeira_sequencia.transcribe()
print(seq_rna)

seq_dna = seq_rna.back_transcribe()
print(seq_dna)


# Tradução

seq_proteina = seq_rna.translate()
seq_proteina_dna = seq_dna.translate()

print(seq_proteina)
print(seq_proteina_dna)


# Analise de Arquivos FASTA

for fasta in SeqIO.parse("fasta.fasta","fasta"):
    print(fasta.id)

    print(fasta.seq)
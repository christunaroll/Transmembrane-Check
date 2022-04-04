# Transmembrane_Check (MCB 185)

Program that predicts if a protein is trans-membrane based on the following properties:
- Signal peptide: 
- Hydrophobic regions(s)
- No prolines in hydrophobic regions (alpha helix)

Hydrophobicity is measued via Kyte-Dolittle. For this program:
- Signal peptide is 8 aa long, KD > 2.5, first 30 aa
- Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

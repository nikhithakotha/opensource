def determine_winner(vignesh_move, charan_move):
    if (vignesh_move == 'R' and charan_move == 'P') or \
       (vignesh_move == 'P' and charan_move == 'S') or \
       (vignesh_move == 'S' and charan_move == 'R'):
        return "Charan"    
    if (charan_move == 'R' and vignesh_move == 'P') or \
       (charan_move == 'P' and vignesh_move == 'S') or \
       (charan_move == 'S' and vignesh_move == 'R'):
        return "Vignesh"
        return "NULL"
vignesh, charan = input().split()
print(determine_winner(vignesh, charan))

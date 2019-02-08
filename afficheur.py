class Afficheur:

    def __init__(self):
        self.grille = None

    def afficher(self, grille):
        self.grille = grille
        if not self.__is_size_valide():
            raise IndexError("La grille n'a pas la bonne taille !")

        for i in range(6):
            for j in range(7):
                if grille[i][j] == '' or grille[i][j] == ' ':
                    grille[i][j] = '~'

        self.grille = [['0', '1', '2', '3', '4', '5', '6']] + self.grille
        
        for i in range(6):
            print(grille[i])
        try:
            import tabulate
            print(tabulate.tabulate(self.grille, tablefmt='fancy_grid'))
        except ImportError:
            for i in range(6):
                print(grille[i])

    def __is_size_valide(self):
        if len(self.grille) != 6:
            return False
        for i in range(6):
            if len(self.grille[i]) != 7:
                return False
        return True


if __name__ == '__main__':
    grille = []
    grille.append(['', '', '', '', '', '', ''])
    grille.append(['', '', '', '', '', '', ''])
    grille.append(['', '', '', '', '', '', ''])
    grille.append(['', '', '', '', '', '', ''])
    grille.append(['', 'X', '', '', '', '', 'X'])
    grille.append(['X', 'O', 'X', '', '', '', 'X'])
    aff = Afficheur()
    aff.afficher(grille)

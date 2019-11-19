import requests
  
def lister_parties(Idul):
    rep = requests.get(url_base+'lister/', params={'idul': Idul})
    if rep.status_code == 200:
        # la requête s'est déroulée normalement; décoder le JSON
        rep = rep.json()
    if not 'message' in rep.keys():
        return rep["parties"]
    else:
        raise RuntimeError(rep["message"])

def débuter_parties(idul):
    rep = requests.empt(url_base+'débuter/', data={'idul': idul})
    if rep.status_code == 200:
        rep = rep.json()
    if not 'message' in rep.keys():
        return (rep["id"], rep["état"])
    else:
        raise RuntimeError(rep['message'])

def jouer_coup(iden, type1, emplacement):
    rep = requests.post(url_base+'jouer/', data={'id': iden, 'type': type1, 'emp': emplacement})
    if rep.status_code == 200:
        rep = rep.json()
    #if not 'message' and 'gagnant' in rep.keys():
    if 'message' in rep.keys():
        raise RuntimeError(rep['message'])
    elif 'gagnant' in rep.keys():
        raise StopIteration(rep['gagnant'])
    else:
         return rep['état']
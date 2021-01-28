import couchbase
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.n1ql import N1QLQuery
from couchbase.exceptions import NotFoundError


def couchConnect():
    cluster = Cluster('couchbase://myserver')
    authenticator = PasswordAuthenticator('username', 'password')
    cluster.authenticate(authenticator)
    cb = cluster.open_bucket('mybucket')
    return cb
 
 
def getDoc(id, bkt):
    try:
        rv = bkt.get(id)
        return rv.value
    except NotFoundError as e:
        print('Item not found : ' + id)
        return ''
    except Exception as err:
        print('error occured ' + str(err) + ' for ' + id)
        return ''
 def extract(cb):
    q = N1QLQuery('myquery')
    r=cb.n1ql_query(q)
    results = []
    for row in r:
        results.append(row['myfield'])
    return results

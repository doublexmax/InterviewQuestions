"""
TOPIC: UNIT CONVERSION 
SUBJECTS: Graph Traversal/Representation, Memoization

This question came from: https://www.youtube.com/watch?v=V8DGdPkBBxg

This question regards answering queries of exchaning a value from one unit to another, or determining if that conversion is impossible.
There is no points for parsing; the facts & queries are provided as tuples.

We can solve this question be essentially creating a graph, with the a node representing a unit and its edges being the units it can convert to as given from the facts.
From here, all we have to do is basically a DFS and go from our node we are converting from to the node representing the unit we are attempting to convert to. If no path is found, then we say "not convertible".

Once the graph (represented via dic, with key = node and value = list of edges) is made, we run DFS with basic memoization through the seenUnits arr.

"""


"""
example facts:
	m = 3.28 ft
	ft = 12 in
	hr = 60 min
	min = 60 sec
example queries:
	2 m = ? in -> answer = 78.72
	13 in = ? m -> "answer = 0.330 (roughly)"
	13 in = ? hr -> "not convertible!"

('m', 3.28, 'ft')
('ft', 12, 'in')
('hr', 60, 'min')
('min', 60, 'sec')

&

(2, 'm', 'in')
(13, 'in', 'm')
(13, 'in', 'hr')
"""

def convertUnits(facts, queries):
	response = []
	seenUnits = []
	dic = {}

	for fact in facts:
		unitFrom = fact[0]
		unitVal = fact[1]
		unitTo = fact[2]
		if dic.get(unitFrom, None) is None:
			dic[unitFrom] = [(unitVal, unitTo)]
		else:
			dic[unitFrom].append((unitVal, unitTo))
		if dic.get(unitTo, None) is None:
			dic[unitTo] = [(1/unitVal, unitFrom)]
		else:
			dic[unitFrom].append((1.0/unitVal, unitFrom))

	for query in queries:
		seenUnits = []
		if query[1] == query[2]:
			response.append(x)
		else:
			response.append(convert(query[1], query[2], query[0], seenUnits, dic))

	return response


def convert(convertFrom, convertTo, x, seenUnits, dic):
	for unit in dic[convertFrom]:
		uVal = unit[0]
		uName = unit[1]

		if uName in seenUnits:
			continue
		
		if uName == convertTo:
			return uVal * x
		
		seenUnits.append(uName)

		seekFurther = convert(uName, convertTo, uVal, seenUnits, dic)

		if seekFurther != "not convertible!":
			return seekFurther * x

	return "not convertible!"

if "__main__" == __name__:
	facts, queries = [], []

	facts.append(('m', 3.28, 'ft'))
	facts.append(('ft', 12, 'in'))
	facts.append(('hr', 60, 'min'))
	facts.append(('min', 60, 'sec'))

	queries.append((2, 'm', 'in'))
	queries.append((13, 'in', 'm'))
	queries.append((13, 'in', 'hr'))

	print(convertUnits(facts, queries))
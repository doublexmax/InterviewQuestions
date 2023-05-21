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
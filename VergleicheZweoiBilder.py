def img_equal(i1, i2, o_grenze = None, u_grenze = None):

	assert i1.mode == i2.mode, "Different kinds of images."

	assert i1.size == i2.size, "Different sizes."

	pairs = izip(i1.getdata(), i2.getdata())

	if len(i1.getbands()) == 1:

		dif = sum(abs(p1-p2) for p1,p2 in pairs)

	else:

		dif = sum(abs(c1-c2) for p1,p2 in pairs for c1,c2 in zip(p1,p2))

	ncomponents = i1.size[0] * i1.size[1] * 3 diff = 100 - ((dif / 255.0 * 100) / ncomponents)

	if o_grenze and u_grenze:

		if diff >= u_grenze and diff <= o_grenze:

			return (True, diff)

		else:

			return (False, diff)

	else:

		return diff
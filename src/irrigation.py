def irrigation_advice(moisture):

    if moisture < 30:
        return "Irrigation Needed"

    elif moisture < 60:
        return "Moderate Water Level"

    else:
        return "No Irrigation Needed"

 if len(security) < time*2+1:
            return []

        result = []
        decSince = [0] * len(security)
        incSince = [0] * len(security)

        for i in range(1, len(security)):
            if security[i] < security[i-1]:
                decSince[i] = decSince[i-1] + 1
                incSince[i] = 0
            elif security[i] > security[i-1]:
                decSince[i] = 0
                incSince[i] = incSince[i - 1] + 1
            else:
                decSince[i] = decSince[i - 1] + 1
                incSince[i] = incSince[i - 1] + 1

        for i in range(time, len(security) - time, 1):
            if decSince[i] >= time and incSince[i + time] >= time:
                result.append(i)

        return result

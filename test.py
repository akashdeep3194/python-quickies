class Beacon:
    def __init__(self, id, str, dir):
        self.Id = id
        self.strength = str
        self.direction = dir


def GetTargetBeacon(beacons):
    max_strength = 0
    for ele in beacons:
        if ele.direction == "B":  # only those beacons who are in the Back
            if ele.strength > max_strength:
                max_strength = ele.strength

                target_beacon = ele
    return target_beacon

#Define inputs
student1_beacons = [Beacon("B3", 2, "B"), Beacon("B2", 5, "F")]
student2_beacons = [Beacon("B3", 2, "B"), Beacon("B2", 5, "B")]
student3_beacons = [Beacon("B3", 2, "B"), Beacon("B2", 4, "B"), Beacon("B3",4,"F")]

# Call the function

print(GetTargetBeacon(student1_beacons).Id)
print(GetTargetBeacon(student2_beacons).Id)
print(GetTargetBeacon(student3_beacons).Id)


def help(section):
    if section == 0:                            # 0 = Ketika di Lobby
        print("Aksi yang dapat dilakukan:")
        print("- explore")
        print("- status")
        print("- switch city")
        print("- shopping")
        print("- save")
        print("- exit")
        print("- alduskuy")
        print("- list sidequest")
    
    elif section == 1:                          # 1 = Ketika didalam Pertarungan
        print("Aksi yang dapat dilakukan:")
        print("- strike")
        print("- magic")
        print("- flee")
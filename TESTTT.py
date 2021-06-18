elif curinput == 'enter':
            # Checks if userinput is enter
                i.position_x = xPos
                i.position_y = yPos
                used = False

                if rotation == 'hori':
                # Sets ship (current object) rotation and moves current location
                    for j in range(size):
                        if matchfield[yPos,xPos+j] == 1:
                            used = True

                    if used == False:
                        i.rotation = "hori"
                        yPos += 1
                        matchfield[yPos, xPos:xPos+next_ship.size] = 1
                    else: print("test")

                else:
                    for j in range(next_ship.size):
                        if matchfield[yPos+j,xPos] == 1:
                            used = True
                            
                    if used == False:
                        i.rotation = "verti"
                        xPos += 1
                        matchfield[yPos:yPos+next_ship.size, xPos] = 1
                    else: print("test")

                if used == False:
                    ship_list_placed.append(i)
                    update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
                    break
                else: print("test")
                
            update_matchfield(game_y_pos, game_x_pos, matchfield, screen)
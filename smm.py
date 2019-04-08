# CMPUT 497 Project
# Six Men's Morris Player
# By Ryan De Forest
# Winter 2019

import random
import os

INF = 9999
NEGINF = -9999
DEPTH_LIMIT = 6


#clear console screen
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#convert coordinate system to index of gameboard array
def movetoindex(idx):
	if idx == 'a1':
		return 0
	elif idx == 'c1':
		return 1
	elif idx == 'e1':
		return 2
	elif idx == 'b2':
		return 3
	elif idx == 'c2':
		return 4
	elif idx == 'd2':
		return 5
	elif idx == 'a3':
		return 6
	elif idx == 'b3':
		return 7
	elif idx == 'd3':
		return 8
	elif idx == 'e3':
		return 9
	elif idx == 'b4':
		return 10
	elif idx == 'c4':
		return 11
	elif idx == 'd4':
		return 12
	elif idx == 'a5':
		return 13
	elif idx == 'c5':
		return 14
	elif idx == 'e5':
		return 15
	return None

#convert index of gameboard array to coordinate system
def indextomove(m):
	if m == 0:
		return 'a1'
	elif m == 1:
		return 'c1'
	elif m == 2:
		return 'e1'
	elif m == 3:
		return 'b2'
	elif m == 4:
		return 'c2'
	elif m == 5:
		return 'd2'
	elif m == 6:
		return 'a3'
	elif m == 7:
		return 'b3'
	elif m == 8:
		return 'd3'
	elif m == 9:
		return 'e3'
	elif m == 10:
		return 'b4'
	elif m == 11:
		return 'c4'
	elif m == 12:
		return 'd4'
	elif m == 13:
		return 'a5'
	elif m == 14:
		return 'c5'
	elif m == 15:
		return 'e5'
	return None

#swaps between 1 and 2 to represent current player
def changeturn(c) :
	return c % 2 + 1

#checks if current move has created a string of 3 pieces
def stringcheck(g, m, p):
	strings = []
	
	if m == 0:
		strings = [[0,1,2],[0,6,13]]
	elif m == 1:
		strings = [[0,1,2]]
	elif m == 2:
		strings = [[0,1,2],[2,9,15]]
	elif m == 3:
		strings = [[3,4,5],[3,7,10]]
	elif m == 4:
		strings = [[3,4,5]]
	elif m == 5:
		strings = [[3,4,5],[5,8,12]]
	elif m == 6:
		strings = [[0,6,13]]
	elif m == 7:
		strings = [[3,7,10]]
	elif m == 8:
		strings = [[5,8,12]]
	elif m == 9:
		strings = [[2,9,15]]
	elif m == 10:
		strings = [[3,7,10],[10,11,12]]
	elif m == 11:
		strings = [[10,11,12]]
	elif m == 12:
		strings = [[5,8,12],[10,11,12]]
	elif m == 13:
		strings = [[0,6,13],[13,14,15]]
	elif m == 14:
		strings = [[13,14,15]]
	elif m == 15:
		strings = [[2,9,15],[13,14,15]]
		
	for t in strings:
		if g[t[0]] == p and g[t[1]] == p and g[t[2]] == p:
			return True
			
	return False
	
#returns the valid places a piece can move to
def getvalidmoves(g, m):
	strings = []
	
	if m == 0:
		strings = [1,6]
	elif m == 1:
		strings = [0,2,4]
	elif m == 2:
		strings = [1,9]
	elif m == 3:
		strings = [4,7]
	elif m == 4:
		strings = [1,3,5]
	elif m == 5:
		strings = [4,8]
	elif m == 6:
		strings = [0,7,13]
	elif m == 7:
		strings = [3,6,10]
	elif m == 8:
		strings = [5,9,12]
	elif m == 9:
		strings = [2,8,15]
	elif m == 10:
		strings = [7,11]
	elif m == 11:
		strings = [10,12,14]
	elif m == 12:
		strings = [8,11]
	elif m == 13:
		strings = [6,14]
	elif m == 14:
		strings = [11,13,15]
	elif m == 15:
		strings = [9,14]
		
	valid = []
	
	for t in strings:
		if g[t] == 0:
			valid.append(t)
			
	return valid

#checks if either player has 2 or less pieces and thus loses
def checkpieces(g):
	p1,p2 = 0,0
	
	for v in g:
		if v == 1:
			p1 += 1
		if v == 2:
			p2 += 1
			
	if p1 <= 2:
		return 1
	elif p2 <= 2:
		return 2
		
	return 0
	
#checks if either player has no valid moves and thus loses
def checkmoves(g):
	p1,p2 = False,False
	
	for v in range(16):
		if g[v] != 0:
			move_list = getvalidmoves(g,v)
			if move_list:
				if g[v] == 1:
					p1 = True
				elif g[v] == 2:
					p2 = True
			if p1 and p2:
				return 0
	if not p1:
		return 1
	elif not p2:
		return 2
		
	return None
	
#checks if removing the selected piece is valid
def checkvalidremoval(g,m,p):
	p = changeturn(p)
	r = getpieces(g,p)		
	flag = True
	
	for v in r:
		if not stringcheck(g,v,p):
			flag = False
			break
			
	if flag:
		return True
		
	if stringcheck(g,m,p):
		return False
	
	return True
	
#gets all indexes of the pieces for the given player
def getpieces(g,p):
	r = []
	
	for v in range(16):
		if g[v] == p:
			r.append(v)
	return r

#display functions for program
def printphase(m):
	if (m < 12):
		print('Setup Phase: Place pieces\n')
	else:
		print('Regular Phase: Move pieces\n')
			
def printheader():
	print('Six Men\'s Morris Player')
	print('CMPUT 497 Project')
	print('by Ryan De Forest\n')
	
def displaygame(g):
	print('   A     B     C     D     E')
	print('1  {}-----------{}-----------{}'.format(itos(g[0]),itos(g[1]),itos(g[2])))
	print('   |           |           |')
	print('   |           |           |')
	print('2  |     {}-----{}-----{}     |'.format(itos(g[3]),itos(g[4]),itos(g[5])))
	print('   |     |           |     |')
	print('   |     |           |     |')
	print('3  {}-----{}           {}-----{}'.format(itos(g[6]),itos(g[7]),itos(g[8]),itos(g[9])))
	print('   |     |           |     |')
	print('   |     |           |     |')
	print('4  |     {}-----{}-----{}     |'.format(itos(g[10]),itos(g[11]),itos(g[12])))
	print('   |           |           |')
	print('   |           |           |')
	print('5  {}-----------{}-----------{}\n'.format(itos(g[13]),itos(g[14]),itos(g[15])))
	
#	print('   A     B     C     D     E')
#	print('1  _-----------_-----------_')
#	print('   |           |           |')
#	print('   |           |           |')
#	print('2  |     _-----_-----_     |')
#	print('   |     |           |     |')
#	print('   |     |           |     |')
#	print('3  _-----_           _-----_')
#	print('   |     |           |     |')
#	print('   |     |           |     |')
#	print('4  |     _-----_-----_     |')
#	print('   |           |           |')
#	print('   |           |           |')
#	print('5  _-----------_-----------_\n')

#converts index value to character for displaying the gameboard
def itos(i):
	if i == 0:
		return '_'
	if i == 1:
		return 'X'
	if i == 2:
		return 'O'
	return None
	
#refresh screen with updated game information
def refresh(g):
	cls()
	printheader()
	displaygame(g)
	
#hueristic calculates players strings(Morrises) against the opponents	
def countStrings(g, p):
	strings = [[0,1,2],[0,6,13],[2,9,15],[3,4,5],[3,7,10],[5,8,12],[10,11,12],[13,14,15]]
	score = 0
	opponent = changeturn(p)
	
	for v in strings:
		if v[0] == v[1] and v[1] == v[2] and v[0] == p:
			score += 1
		elif v[0] == v[1] and v[1] == v[2] and v[0] == opponent:
			score -= 1
	return score

#heuristic calculates blocked opponent pieces against players	
def countBlocked(g, p):
	score = 0
	opponent = changeturn(p)
	for v in range(16):
		if g[v] != 0:
			if not getvalidmoves(g,v):
				if g[v] == opponent:
					score += 1
				else:
					score -= 1
	return score
	
#heuristic calculates player's pieces against opponenet's
def countPieces(g, p):
	opponent = changeturn(p)
	score = 0
	
	for v in range(16):
		if g[v] == p:
			score += 1
		elif g[v] == opponent:
			score -= 1
	return score
	
#heuristic calculates number of 2 strings that can be completed against opponent's set
def count2(g, p):
	opponent = changeturn(p)
	strings = [[0,1,2],[0,6,13],[2,9,15],[3,4,5],[3,7,10],[5,8,12],[10,11,12],[13,14,15]]
	score = 0
	
	for v in strings:
		if v[0] == v[1] and v[2] == 0:
			if v[0] == p:
				score += 1
			elif v[0] == opponent:
				score -= 1
		elif v[0] == v[2] and v[1] == 0:
			if v[0] == p:
				score += 1
			elif v[0] == opponent:
				score -= 1
		elif v[1] == v[2] and v[0] == 0:
			if v[1] == p:
				score += 1
			elif v[1] == opponent:
				score -= 1
				
	return score

#heuristic determines if position is in a win/loss state
def checkWin(g, p):	
	result = checkpieces(g)
	opponent = changeturn(p)
			
	if result == opponent:
		return 1
	elif result == p:
		return -1
		
	result = checkmoves(g)
	
	if result == opponent:
		return 1
	elif result == p:
		return -1
	
	return 0

#calculates linear heuristic for a given board position	
def getHeuristic(g, p, moves):
	#1 number of morrises, difference
	h1 = countStrings(g, p)
	#2 number of trapped opponent pieces
	h2 = countBlocked(g, p)
	#3 number of pieces, difference
	h3 = countPieces(g, p)
	
	if moves < 12:
		#4 number of 2pc configurations, difference
		h4 = count2(g, p)
		return h1 * 26 + h2 * 1 + h3 * 9 + h4 * 10
	else:
		#5 winning position
		h5 = checkWin(g, p)
		return h1 * 43 + h2 * 10 + h3 * 11 + h5 * 1086

#gets all possible children positions from a given board position for the current player		
def getChildren(g, p, moves):
	children = []
	opponent = changeturn(p)
	if moves < 12:
		for v in range(16):
			if g[v] == 0:
				tmp = g[:]
				tmp[v] = p
				if stringcheck(tmp, v, p):
					for t in getpieces(tmp, opponent):
						if checkvalidremoval(tmp, t , p):
							tmp[t] = 0
							children.append(tmp)
				else:
					children.append(tmp)
	else:
		for v in getpieces(g, p):
			for t in getvalidmoves(g, v):
				tmp = g[:]
				tmp[v] = 0
				tmp[t] = p
				if stringcheck(tmp, t, p):
					for s in getpieces(tmp, opponent):
						if checkvalidremoval(tmp, s , p):
							tmp[s] = 0
							children.append(tmp)
				else:
					children.append(tmp)
					
	return children
	
#gets all possible children positions with the move from a given board position for the current player
def getChildrenMoves(g, p, moves):
	children = []
	opponent = changeturn(p)
	if moves < 12:
		for v in range(16):
			if g[v] == 0:
				tmp = g[:]
				tmp[v] = p
				if stringcheck(tmp, v, p):
					for t in getpieces(tmp, opponent):
						if checkvalidremoval(tmp, t , p):
							tmp[t] = 0
							children.append([tmp,(v,t)])
				else:
					children.append([tmp,(v,)])
	else:
		for v in getpieces(g, p):
			for t in getvalidmoves(g, v):
				tmp = g[:]
				tmp[v] = 0
				tmp[t] = p
				if stringcheck(tmp, t, p):
					for s in getpieces(tmp, opponent):
						if checkvalidremoval(tmp, s , p):
							tmp[s] = 0
							children.append([tmp,(v,t,s)])
				else:
					children.append([tmp,(v,t)])
	return children

#alpha beta search tree for the ai player to calculate the best move option	
def alphabeta(node, depth, alpha, beta, maxPlayer, moves, p, isFirst):
	if depth == 0 or (checkWin(node, p) != 0 and moves >= 12):
		return getHeuristic(node, p, moves)
	if maxPlayer:
		if isFirst:
			value = NEGINF
			bestMove = 0
			for c in getChildrenMoves(node, p, moves):
				tmpValue = alphabeta(c[0], depth - 1, alpha, beta, False, moves+1, p, False)
				if tmpValue > value:
					value = tmpValue
					bestMove = c[1]
				alpha = max(alpha, value)
				if alpha >= beta:
					break 
			return bestMove
		else:
			value = NEGINF
			for c in getChildren(node, p, moves):
				value = max(value, alphabeta(c, depth - 1, alpha, beta, False, moves+1, p, False))
				alpha = max(alpha, value)
				if alpha >= beta:
					break 
			return value
	else:
		opponent = changeturn(p)
		value = INF
		for c in getChildren(node, opponent, moves):
			value = min(value, alphabeta(c, depth - 1, alpha, beta, True, moves+1, p, False))
			beta = min(beta, value)
			if alpha >= beta:
				break
		return value
	
#main function the program runs from	
def main():	
	gameboard = [0] * 16
	player,ai = 0,0
	cur_player = 1
	moves = 0
	status = ''
		
	printheader()
	
	while True:
		data = input('Do you want to play as first(X) or second(O) player? ')
		if data.lower() == 'x':
			player,ai = 1,2
			break
		elif data.lower() == 'o':
			player,ai = 2,1
			break
		else:
			print("Invalid input, please enter either X to go first, or O to go second.")
	
	while True:
		refresh(gameboard)
		printphase(moves)
			
		if (moves < 12): #setup phase
			if cur_player == player: #player
				while True:
					idx = movetoindex(input('Please make a move (eg: a3): '))
					if idx != None:
						if (gameboard[idx] == 0):
							gameboard[idx] = player
							moves += 1
							status = 'You have played at {}\n'.format(indextomove(idx))
							if stringcheck(gameboard, idx, player):
								refresh(gameboard)
								while True:
									print('You have made a string and can remove one of your opponent\'s pieces\nNote: you cannot remove a piece that is part of a string unless no other piece is available\n')
									idx = movetoindex(input('Please select a piece to remove: '))
									if idx != None:
										if gameboard[idx] == ai and checkvalidremoval(gameboard, idx, player):
											status += 'You have removed one of your opponent\'s pieces at {}\n'.format(indextomove(idx))
											gameboard[idx] = 0
											break
										else:
											print('Invalid removal, please try again\n')
									else:
										print('Invalid removal, please try again\n')
													
							break
						else:
							print('Invalid move, please try again\n')
					else:
						print('Invalid move, please try again\n')
			else:
				find_move = alphabeta(gameboard, DEPTH_LIMIT, NEGINF, INF, True, moves, ai, True)
				print(find_move)
				moves += 1
				if len(find_move) == 1:
					gameboard[find_move[0]] = ai
					status = 'The AI has played at {}\n'.format(indextomove(find_move[0]))
				elif len(find_move) == 2:
					gameboard[find_move[0]] = ai
					gameboard[find_move[1]] = 0
					status = 'The AI has played at {}\n'.format(indextomove(find_move[0]))
					status += 'The AI has made a string and removed your piece at {}\n'.format(indextomove(find_move[1]))
				#while True: #random AI
				#	idx = random.randint(0,15)					
				#	if (gameboard[idx] == 0):
				#		gameboard[idx] = ai
				#		moves += 1
				#		status = 'The AI has played at {}\n'.format(indextomove(idx))
				#		if stringcheck(gameboard, idx, ai):
				#			while True:
				#				idx = random.randint(0,15)								
				#				if gameboard[idx] == player and checkvalidremoval(gameboard, idx, ai):
				#					status += 'The AI has made a string and removed your piece at {}\n'.format(indextomove(idx))
				#					gameboard[idx] = 0
				#					break
				#		break
		else: #regular phase
			if cur_player == player:			
				while True:
					idx = movetoindex(input('Please select a piece to move (eg: a3): '))
					if idx != None:
						listofmoves = getvalidmoves(gameboard,idx)
						if gameboard[idx] == player and listofmoves:
							loc = movetoindex(input('Please select an open location to move to (eg: a5): '))
							if loc in listofmoves:
								gameboard[idx] = 0
								gameboard[loc] = player
								status = 'You have moved your piece from {} to {}\n'.format(indextomove(idx),indextomove(loc))
								if stringcheck(gameboard, loc, player):
									refresh(gameboard)
									while True:
										print('You have made a string and can remove one of your opponent\'s pieces\nNote: you cannot remove a piece that is part of a string unless no other piece is available\n')
										idx = movetoindex(input('Please select an opponents piece to remove: '))
										if idx != None:
											if gameboard[idx] == ai and checkvalidremoval(gameboard, idx, player):
												status += 'You have removed one of your opponent\'s pieces at {}\n'.format(indextomove(idx))
												gameboard[idx] = 0
												break
											else:
												print('Invalid removal, please try again\n')
										else:
											print('Invalid removal, please try again\n')
								moves += 1
								break
							else:
								print('Invalid location to move to, please try again\n')
						else:
							print('Did not select one of your pieces or had no valid moves, please try again\n')
					else:
						print('Did not select one of your pieces or had no valid moves, please try again\n')
			
			else:
				find_move = alphabeta(gameboard, DEPTH_LIMIT, NEGINF, INF, True, moves, ai, True)
				moves += 1
				if len(find_move) == 2:
					gameboard[find_move[0]] = 0
					gameboard[find_move[1]] = ai
					status = 'The AI has moved a piece from {} to {}\n'.format(indextomove(find_move[0]), indextomove(find_move[1]))	
				elif len(find_move) == 3:
					gameboard[find_move[0]] = 0
					gameboard[find_move[1]] = ai
					gameboard[find_move[2]] = 0
					status = 'The AI has moved a piece from {} to {}\n'.format(indextomove(find_move[0]), indextomove(find_move[1]))
					status += 'The AI has made a string and removed your piece at {}\n'.format(indextomove(find_move[2]))
			#	while True:  #random AI
			#		idx = random.randint(0,15)					
			#		if gameboard[idx] == ai:
			#			listofmoves = getvalidmoves(gameboard,idx)
			#			if listofmoves:
			#				loc = random.randint(0,len(listofmoves)-1)
			#				status = 'The AI has moved a piece from {} to {}\n'.format(indextomove(idx), indextomove(listofmoves[loc]))							
			#				gameboard[idx] = 0
			#				gameboard[listofmoves[loc]] = ai
			#				if stringcheck(gameboard, idx, ai):
			#					while True:
			#						idx = random.randint(0,15)
			#						if gameboard[idx] == player and checkvalidremoval(gameboard, idx, ai):
			#							status += 'The AI has made a string and removed your piece at {}\n'.format(indextomove(idx))
			#							gameboard[idx] = 0
			#							break
			#				break
			
		refresh(gameboard)			
		print(status)
		input('Press enter to continue')
		
		if moves >= 12:		
			result = checkpieces(gameboard)
			
			if result != 0:
				if player == result:
					print('The AI wins! You only have 2 pieces left\n')
				else:
					print('You win! The AI only has 2 pieces left\n')
				input('Press enter to exit the game')
				exit()
				
			result = checkmoves(gameboard)
			
			if result != 0:
				if player == result:
					print('The AI wins! You only have no valid moves left\n')
				else:
					print('You win! The AI has no valid moves left\n')
				input('Press enter to exit the game')
				exit()
						
		cur_player = changeturn(cur_player)

main()
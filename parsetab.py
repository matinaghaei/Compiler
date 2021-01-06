
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftORleftANDleftNOTleftEXPleftGTLTNEEQLEGErightASSIGNleftMODleftSUMSUBleftMULDIVleftIFREDUCEleftELSEELSEIFAND ASSIGN BOOLEAN COLON COMMA DIV ELSE ELSEIF EQ ERROR FALSE FLOAT FLOATNUMBER FOR FUNCTION GE GT ID IF IN INTEGER INTEGERNUMBER LCB LE LRB LSB LT MAIN MOD MUL NE NOT ON OR PRINT RCB RETURN RRB RSB SEMICOLON SUB SUM TRUE WHERE WHILEprogram : declist MAIN LRB RRB block\n        declist :\n        \n        declist : declist dec\n        \n        dec : vardec\n        \n        vardec : idlist COLON type SEMICOLON\n        \n        type : INTEGER\n        type : FLOAT\n        type : BOOLEAN\n        \n        iddec : ID\n        \n        iddec : ID ASSIGN exp\n        \n        iddec : ID LSB exp RSB\n        \n        idlist : iddec\n        \n        idlist : idlist COMMA iddec\n        exp : ID ASSIGN exp\n        exp : exp SUM exp\n        exp : exp SUB exp\n        exp : exp DIV exp\n        exp : exp MOD exp\n        exp : exp MUL exp\n        exp : constexp : IDexp : ID LSB exp RSBexp : ID LSB exp RSB ASSIGN expexp : SUB expexp : LRB exp RRB\n        const : FLOATNUMBER\n        const : INTEGERNUMBER\n        \n        explist : exp\n        \n        explist : explist COMMA exp\n        \n        block : LCB stmtlist RCB\n        \n        stmtlist : stmtlist stmt\n        stmtlist :\n        stmt : exp SEMICOLON\n        \n        stmt : block\n        \n        stmt : vardec\n        \n        stmt : PRINT LRB ID RRB SEMICOLON\n        \n        case : WHERE const COLON stmtlist\n        \n        cases : cases case\n        cases :\n        stmt : IF LRB exp RRB stmt elseiflist %prec IFREDUCEstmt : WHILE LRB exp RRB stmtstmt : IF LRB exp RRB stmt elseiflist ELSE stmtstmt : FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt\n        stmt : ON LRB exp RRB LCB cases RCB SEMICOLON\n\n        stmt : FOR LRB ID IN ID RRB stmt\n        \n        elseiflist : elseiflist ELSEIF LRB exp RRB stmt\n        elseiflist :exp : relopexp %prec EXP\n        relopexp : exp GT exp\n        relopexp : exp LT exp\n        relopexp : exp NE exp\n        relopexp : exp EQ exp\n        relopexp : exp LE exp\n        relopexp : exp GE exp\n        \n        relopexp : relopexp GT exp\n        relopexp : relopexp LT exp\n        relopexp : relopexp NE exp\n        relopexp : relopexp EQ exp\n        relopexp : relopexp LE exp\n        relopexp : relopexp GE exp\n        exp : exp AND expexp : exp OR expexp : NOT exp\n        const : TRUE\n        const : FALSE\n        \n        exp : ID LRB explist RRB\n        exp : ID LRB RRB\n        \n        dec : funcdec\n        \n        funcdec : FUNCTION ID LRB paramdecs RRB COLON type block\n        funcdec : FUNCTION ID LRB paramdecs RRB block\n        \n        paramdecs : paramdecslist\n        paramdecs :\n        \n        paramdecslist : paramdec\n        paramdecslist : paramdecslist COMMA paramdec\n        \n        paramdec : ID COLON type\n        paramdec : ID LSB RSB COLON type\n        \n        stmt : RETURN exp SEMICOLON\n        '
    
_lr_action_items = {'MAIN':([0,2,4,5,6,38,99,114,142,],[-2,3,-3,-4,-68,-5,-30,-70,-69,]),'FUNCTION':([0,2,4,5,6,38,99,114,142,],[-2,8,-3,-4,-68,-5,-30,-70,-69,]),'ID':([0,2,4,5,6,8,13,15,16,23,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,73,99,100,102,103,110,114,118,119,120,121,122,123,124,125,126,130,140,142,146,147,148,149,151,152,153,157,158,159,161,164,168,169,170,171,174,175,176,177,178,],[-2,9,-3,-4,-68,14,9,24,24,39,24,24,24,-32,-5,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,105,39,-30,-31,-34,-35,24,-70,24,-33,132,24,24,24,24,138,24,24,-77,-69,105,105,24,155,-36,-47,-41,-40,24,105,105,-45,-42,24,105,-44,-43,-32,105,105,-46,]),'$end':([1,36,99,],[0,-1,-30,]),'LRB':([3,14,15,16,24,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,99,100,102,103,104,105,106,107,108,109,110,118,119,121,122,123,124,125,126,130,138,140,146,147,148,151,152,153,157,158,159,161,162,164,168,169,170,171,174,175,176,177,178,],[11,23,28,28,45,28,28,28,-32,-5,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-30,-31,-34,-35,120,45,123,124,125,126,28,28,-33,28,28,28,28,28,28,28,45,-77,28,28,28,-36,-47,-41,-40,28,28,28,169,-45,-42,28,28,-44,-43,-32,28,28,-46,]),'COLON':([7,9,10,22,24,25,27,29,31,32,33,34,39,59,67,68,72,74,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,112,116,117,133,143,145,172,],[12,-9,-12,-13,-21,-10,-20,-48,-26,-27,-64,-65,70,-24,-63,-11,113,-14,-67,-15,-16,-17,-18,-19,-61,-62,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,-9,128,-22,-66,-10,-23,-11,175,]),'COMMA':([7,9,10,19,20,21,22,24,25,27,29,31,32,33,34,41,42,59,67,68,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,105,111,115,116,117,131,133,141,143,145,],[13,-9,-12,-6,-7,-8,-13,-21,-10,-20,-48,-26,-27,-64,-65,73,-73,-24,-63,-11,-14,118,-67,-28,-15,-16,-17,-18,-19,-61,-62,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,-9,-75,-74,-22,-66,-29,-10,-76,-23,-11,]),'ASSIGN':([9,24,105,116,138,145,],[15,43,121,130,43,130,]),'LSB':([9,24,39,105,138,],[16,44,71,122,44,]),'RRB':([11,19,20,21,23,24,27,29,31,32,33,34,40,41,42,45,59,60,67,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,111,115,116,117,131,132,135,136,139,141,143,155,163,173,],[17,-6,-7,-8,-72,-21,-20,-48,-26,-27,-64,-65,72,-71,-73,77,-24,92,-63,-14,117,-67,-28,-15,-16,-17,-18,-19,-61,-62,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,-75,-74,-22,-66,-29,144,146,147,150,-76,-23,159,170,176,]),'INTEGER':([12,70,113,128,],[19,19,19,19,]),'FLOAT':([12,70,113,128,],[20,20,20,20,]),'BOOLEAN':([12,70,113,128,],[21,21,21,21,]),'SUB':([15,16,24,25,26,27,28,29,30,31,32,33,34,35,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,69,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,110,116,117,118,119,121,122,123,124,125,126,127,130,131,133,134,135,136,137,138,139,140,143,145,146,147,148,151,152,153,154,157,158,159,161,163,164,168,169,170,171,173,174,175,176,177,178,],[26,26,-21,47,26,-20,26,-48,26,-26,-27,-64,-65,47,-32,-5,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-24,47,26,26,26,26,26,26,47,26,47,47,-67,47,-15,-16,-17,47,-19,47,47,47,47,47,47,47,47,-25,47,47,47,47,47,47,-30,-31,47,-34,-35,-21,26,-22,-66,26,-33,26,26,26,26,26,26,47,26,47,47,47,47,47,47,-21,47,-77,47,-22,26,26,26,-36,-47,-41,47,-40,26,26,26,47,-45,-42,26,26,-44,47,-43,-32,26,26,-46,]),'NOT':([15,16,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,99,100,102,103,110,118,119,121,122,123,124,125,126,130,140,146,147,148,151,152,153,157,158,159,161,164,168,169,170,171,174,175,176,177,178,],[30,30,30,30,30,-32,-5,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-30,-31,-34,-35,30,30,-33,30,30,30,30,30,30,30,-77,30,30,30,-36,-47,-41,-40,30,30,30,-45,-42,30,30,-44,-43,-32,30,30,-46,]),'FLOATNUMBER':([15,16,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,99,100,102,103,110,118,119,121,122,123,124,125,126,130,140,146,147,148,151,152,153,157,158,159,161,164,167,168,169,170,171,174,175,176,177,178,],[31,31,31,31,31,-32,-5,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-30,-31,-34,-35,31,31,-33,31,31,31,31,31,31,31,-77,31,31,31,-36,-47,-41,-40,31,31,31,-45,31,-42,31,31,-44,-43,-32,31,31,-46,]),'INTEGERNUMBER':([15,16,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,99,100,102,103,110,118,119,121,122,123,124,125,126,130,140,146,147,148,151,152,153,157,158,159,161,164,167,168,169,170,171,174,175,176,177,178,],[32,32,32,32,32,-32,-5,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-30,-31,-34,-35,32,32,-33,32,32,32,32,32,32,32,-77,32,32,32,-36,-47,-41,-40,32,32,32,-45,32,-42,32,32,-44,-43,-32,32,32,-46,]),'TRUE':([15,16,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,99,100,102,103,110,118,119,121,122,123,124,125,126,130,140,146,147,148,151,152,153,157,158,159,161,164,167,168,169,170,171,174,175,176,177,178,],[33,33,33,33,33,-32,-5,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-30,-31,-34,-35,33,33,-33,33,33,33,33,33,33,33,-77,33,33,33,-36,-47,-41,-40,33,33,33,-45,33,-42,33,33,-44,-43,-32,33,33,-46,]),'FALSE':([15,16,26,28,30,37,38,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,99,100,102,103,110,118,119,121,122,123,124,125,126,130,140,146,147,148,151,152,153,157,158,159,161,164,167,168,169,170,171,174,175,176,177,178,],[34,34,34,34,34,-32,-5,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-30,-31,-34,-35,34,34,-33,34,34,34,34,34,34,34,-77,34,34,34,-36,-47,-41,-40,34,34,34,-45,34,-42,34,34,-44,-43,-32,34,34,-46,]),'LCB':([17,19,20,21,37,38,69,72,99,100,102,103,119,129,140,146,147,150,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[37,-6,-7,-8,-32,-5,37,37,-30,-31,-34,-35,-33,37,-77,37,37,156,-36,-47,-41,-40,37,37,-45,-42,37,-44,-43,-32,37,37,-46,]),'SEMICOLON':([18,19,20,21,24,27,29,31,32,33,34,59,67,74,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,133,137,138,143,144,145,154,165,],[38,-6,-7,-8,-21,-20,-48,-26,-27,-64,-65,-24,-63,-14,-67,-15,-16,-17,-18,-19,-61,-62,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,119,-21,-22,-66,140,-14,148,-21,-23,151,-22,158,171,]),'SUM':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,46,-20,-48,-26,-27,-64,-65,46,-24,46,46,46,46,-67,46,-15,-16,-17,46,-19,46,46,46,46,46,46,46,46,-25,46,46,46,46,46,46,46,-21,-22,-66,46,46,46,46,46,46,46,-21,46,46,-22,46,46,46,]),'DIV':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,48,-20,-48,-26,-27,-64,-65,48,48,48,48,48,48,-67,48,48,48,-17,48,-19,48,48,48,48,48,48,48,48,-25,48,48,48,48,48,48,48,-21,-22,-66,48,48,48,48,48,48,48,-21,48,48,-22,48,48,48,]),'MOD':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,49,-20,-48,-26,-27,-64,-65,49,-24,49,49,49,49,-67,49,-15,-16,-17,-18,-19,49,49,49,49,49,49,49,49,-25,49,49,49,49,49,49,49,-21,-22,-66,49,49,49,49,49,49,49,-21,49,49,-22,49,49,49,]),'MUL':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,50,-20,-48,-26,-27,-64,-65,50,50,50,50,50,50,-67,50,50,50,-17,50,-19,50,50,50,50,50,50,50,50,-25,50,50,50,50,50,50,50,-21,-22,-66,50,50,50,50,50,50,50,-21,50,50,-22,50,50,50,]),'AND':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,51,-20,-48,-26,-27,-64,-65,51,-24,51,-63,-14,51,-67,51,-15,-16,-17,-18,-19,-61,51,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,51,-21,-22,-66,51,51,-14,51,51,51,51,-21,51,-23,-22,51,51,51,]),'OR':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,52,-20,-48,-26,-27,-64,-65,52,-24,52,-63,-14,52,-67,52,-15,-16,-17,-18,-19,-61,-62,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,52,-21,-22,-66,52,52,-14,52,52,52,52,-21,52,-23,-22,52,52,52,]),'GT':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,53,-20,61,-26,-27,-64,-65,53,-24,53,53,-14,53,-67,53,-15,-16,-17,-18,-19,53,53,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,53,-21,-22,-66,53,53,-14,53,53,53,53,-21,53,-23,-22,53,53,53,]),'LT':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,54,-20,62,-26,-27,-64,-65,54,-24,54,54,-14,54,-67,54,-15,-16,-17,-18,-19,54,54,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,54,-21,-22,-66,54,54,-14,54,54,54,54,-21,54,-23,-22,54,54,54,]),'NE':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,55,-20,63,-26,-27,-64,-65,55,-24,55,55,-14,55,-67,55,-15,-16,-17,-18,-19,55,55,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,55,-21,-22,-66,55,55,-14,55,55,55,55,-21,55,-23,-22,55,55,55,]),'EQ':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,56,-20,64,-26,-27,-64,-65,56,-24,56,56,-14,56,-67,56,-15,-16,-17,-18,-19,56,56,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,56,-21,-22,-66,56,56,-14,56,56,56,56,-21,56,-23,-22,56,56,56,]),'LE':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,57,-20,65,-26,-27,-64,-65,57,-24,57,57,-14,57,-67,57,-15,-16,-17,-18,-19,57,57,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,57,-21,-22,-66,57,57,-14,57,57,57,57,-21,57,-23,-22,57,57,57,]),'GE':([24,25,27,29,31,32,33,34,35,59,60,67,74,75,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,101,105,116,117,127,131,133,134,135,136,137,138,139,143,145,154,163,173,],[-21,58,-20,66,-26,-27,-64,-65,58,-24,58,58,-14,58,-67,58,-15,-16,-17,-18,-19,58,58,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,58,-21,-22,-66,58,58,-14,58,58,58,58,-21,58,-23,-22,58,58,58,]),'RSB':([24,27,29,31,32,33,34,35,59,67,71,74,75,77,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,116,117,134,143,],[-21,-20,-48,-26,-27,-64,-65,68,-24,-63,112,-14,116,-67,-15,-16,-17,-18,-19,-61,-62,-49,-50,-51,-52,-53,-54,-25,-55,-56,-57,-58,-59,-60,-22,-66,145,-23,]),'RCB':([37,38,69,99,100,102,103,119,140,151,152,153,156,157,160,164,166,168,171,174,175,177,178,],[-32,-5,99,-30,-31,-34,-35,-33,-77,-36,-47,-41,-39,-40,165,-45,-38,-42,-44,-43,-32,-37,-46,]),'PRINT':([37,38,69,99,100,102,103,119,140,146,147,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[-32,-5,104,-30,-31,-34,-35,-33,-77,104,104,-36,-47,-41,-40,104,104,-45,-42,104,-44,-43,-32,104,104,-46,]),'IF':([37,38,69,99,100,102,103,119,140,146,147,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[-32,-5,106,-30,-31,-34,-35,-33,-77,106,106,-36,-47,-41,-40,106,106,-45,-42,106,-44,-43,-32,106,106,-46,]),'WHILE':([37,38,69,99,100,102,103,119,140,146,147,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[-32,-5,107,-30,-31,-34,-35,-33,-77,107,107,-36,-47,-41,-40,107,107,-45,-42,107,-44,-43,-32,107,107,-46,]),'FOR':([37,38,69,99,100,102,103,119,140,146,147,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[-32,-5,108,-30,-31,-34,-35,-33,-77,108,108,-36,-47,-41,-40,108,108,-45,-42,108,-44,-43,-32,108,108,-46,]),'ON':([37,38,69,99,100,102,103,119,140,146,147,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[-32,-5,109,-30,-31,-34,-35,-33,-77,109,109,-36,-47,-41,-40,109,109,-45,-42,109,-44,-43,-32,109,109,-46,]),'RETURN':([37,38,69,99,100,102,103,119,140,146,147,151,152,153,157,159,161,164,168,170,171,174,175,176,177,178,],[-32,-5,110,-30,-31,-34,-35,-33,-77,110,110,-36,-47,-41,-40,110,110,-45,-42,110,-44,-43,-32,110,110,-46,]),'ELSE':([38,99,102,103,119,140,151,152,153,157,164,168,171,174,178,],[-5,-30,-34,-35,-33,-77,-36,-47,-41,161,-45,-42,-44,-43,-46,]),'ELSEIF':([38,99,102,103,119,140,151,152,153,157,164,168,171,174,178,],[-5,-30,-34,-35,-33,-77,-36,-47,-41,162,-45,-42,-44,-43,-46,]),'WHERE':([38,99,100,102,103,119,140,151,152,153,156,157,160,164,166,168,171,174,175,177,178,],[-5,-30,-31,-34,-35,-33,-77,-36,-47,-41,-39,-40,167,-45,-38,-42,-44,-43,-32,-37,-46,]),'IN':([138,],[149,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'declist':([0,],[2,]),'dec':([2,],[4,]),'vardec':([2,69,146,147,159,161,170,176,177,],[5,103,103,103,103,103,103,103,103,]),'funcdec':([2,],[6,]),'idlist':([2,69,146,147,159,161,170,176,177,],[7,7,7,7,7,7,7,7,7,]),'iddec':([2,13,69,146,147,159,161,170,176,177,],[10,22,10,10,10,10,10,10,10,10,]),'type':([12,70,113,128,],[18,111,129,141,]),'exp':([15,16,26,28,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,110,118,121,122,123,124,125,126,130,146,147,148,158,159,161,169,170,176,177,],[25,35,59,60,67,74,75,78,79,80,81,82,83,84,85,86,87,88,89,90,91,93,94,95,96,97,98,101,127,131,133,134,135,136,137,139,143,101,101,154,163,101,101,173,101,101,101,]),'const':([15,16,26,28,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,110,118,121,122,123,124,125,126,130,146,147,148,158,159,161,167,169,170,176,177,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,172,27,27,27,27,]),'relopexp':([15,16,26,28,30,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,61,62,63,64,65,66,69,110,118,121,122,123,124,125,126,130,146,147,148,158,159,161,169,170,176,177,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'block':([17,69,72,129,146,147,159,161,170,176,177,],[36,102,114,142,102,102,102,102,102,102,102,]),'paramdecs':([23,],[40,]),'paramdecslist':([23,],[41,]),'paramdec':([23,73,],[42,115,]),'stmtlist':([37,175,],[69,177,]),'explist':([45,],[76,]),'stmt':([69,146,147,159,161,170,176,177,],[100,152,153,164,168,174,178,100,]),'elseiflist':([152,],[157,]),'cases':([156,],[160,]),'case':([160,],[166,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> declist MAIN LRB RRB block','program',5,'p_program','pars.py',16),
  ('declist -> <empty>','declist',0,'p_declist_empty','pars.py',22),
  ('declist -> declist dec','declist',2,'p_declist','pars.py',28),
  ('dec -> vardec','dec',1,'p_dec_vardec','pars.py',35),
  ('vardec -> idlist COLON type SEMICOLON','vardec',4,'p_vardec','pars.py',41),
  ('type -> INTEGER','type',1,'p_type','pars.py',47),
  ('type -> FLOAT','type',1,'p_type','pars.py',48),
  ('type -> BOOLEAN','type',1,'p_type','pars.py',49),
  ('iddec -> ID','iddec',1,'p_iddec_ID','pars.py',55),
  ('iddec -> ID ASSIGN exp','iddec',3,'p_iddec_assign','pars.py',62),
  ('iddec -> ID LSB exp RSB','iddec',4,'p_iddec_array','pars.py',68),
  ('idlist -> iddec','idlist',1,'p_idlist','pars.py',74),
  ('idlist -> idlist COMMA iddec','idlist',3,'p_idlist_comma','pars.py',80),
  ('exp -> ID ASSIGN exp','exp',3,'p_exp_assign','pars.py',85),
  ('exp -> exp SUM exp','exp',3,'p_exp_arithmetic','pars.py',90),
  ('exp -> exp SUB exp','exp',3,'p_exp_arithmetic','pars.py',91),
  ('exp -> exp DIV exp','exp',3,'p_exp_arithmetic','pars.py',92),
  ('exp -> exp MOD exp','exp',3,'p_exp_arithmetic','pars.py',93),
  ('exp -> exp MUL exp','exp',3,'p_exp_arithmetic','pars.py',94),
  ('exp -> const','exp',1,'p_exp_const','pars.py',99),
  ('exp -> ID','exp',1,'p_exp_ID','pars.py',103),
  ('exp -> ID LSB exp RSB','exp',4,'p_exp_array','pars.py',107),
  ('exp -> ID LSB exp RSB ASSIGN exp','exp',6,'p_lvalue','pars.py',111),
  ('exp -> SUB exp','exp',2,'p_exp_sub','pars.py',115),
  ('exp -> LRB exp RRB','exp',3,'p_exp_par','pars.py',119),
  ('const -> FLOATNUMBER','const',1,'p_const_arithmetic','pars.py',124),
  ('const -> INTEGERNUMBER','const',1,'p_const_arithmetic','pars.py',125),
  ('explist -> exp','explist',1,'p_explist','pars.py',132),
  ('explist -> explist COMMA exp','explist',3,'p_explist_comma','pars.py',138),
  ('block -> LCB stmtlist RCB','block',3,'p_block','pars.py',144),
  ('stmtlist -> stmtlist stmt','stmtlist',2,'p_stmtlist','pars.py',150),
  ('stmtlist -> <empty>','stmtlist',0,'p_stmtlist_empty','pars.py',155),
  ('stmt -> exp SEMICOLON','stmt',2,'p_stmt_sem','pars.py',160),
  ('stmt -> block','stmt',1,'p_stmt_block','pars.py',166),
  ('stmt -> vardec','stmt',1,'p_stmt_var','pars.py',172),
  ('stmt -> PRINT LRB ID RRB SEMICOLON','stmt',5,'p_stmt_print','pars.py',178),
  ('case -> WHERE const COLON stmtlist','case',4,'p_case','pars.py',186),
  ('cases -> cases case','cases',2,'p_cases','pars.py',192),
  ('cases -> <empty>','cases',0,'p_cases','pars.py',193),
  ('stmt -> IF LRB exp RRB stmt elseiflist','stmt',6,'p_stmt_if','pars.py',201),
  ('stmt -> WHILE LRB exp RRB stmt','stmt',5,'p_stmt_while','pars.py',205),
  ('stmt -> IF LRB exp RRB stmt elseiflist ELSE stmt','stmt',8,'p_stmt_if_else','pars.py',209),
  ('stmt -> FOR LRB exp SEMICOLON exp SEMICOLON exp RRB stmt','stmt',9,'p_stmt_for','pars.py',213),
  ('stmt -> ON LRB exp RRB LCB cases RCB SEMICOLON','stmt',8,'p_stmt_control','pars.py',218),
  ('stmt -> FOR LRB ID IN ID RRB stmt','stmt',7,'p_stmt_control','pars.py',220),
  ('elseiflist -> elseiflist ELSEIF LRB exp RRB stmt','elseiflist',6,'p_elseiflist','pars.py',226),
  ('elseiflist -> <empty>','elseiflist',0,'p_elseiflist_empty','pars.py',231),
  ('exp -> relopexp','exp',1,'p_exp_relop','pars.py',235),
  ('relopexp -> exp GT exp','relopexp',3,'p_relopexp','pars.py',240),
  ('relopexp -> exp LT exp','relopexp',3,'p_relopexp','pars.py',241),
  ('relopexp -> exp NE exp','relopexp',3,'p_relopexp','pars.py',242),
  ('relopexp -> exp EQ exp','relopexp',3,'p_relopexp','pars.py',243),
  ('relopexp -> exp LE exp','relopexp',3,'p_relopexp','pars.py',244),
  ('relopexp -> exp GE exp','relopexp',3,'p_relopexp','pars.py',245),
  ('relopexp -> relopexp GT exp','relopexp',3,'p_relopexp_rel','pars.py',251),
  ('relopexp -> relopexp LT exp','relopexp',3,'p_relopexp_rel','pars.py',252),
  ('relopexp -> relopexp NE exp','relopexp',3,'p_relopexp_rel','pars.py',253),
  ('relopexp -> relopexp EQ exp','relopexp',3,'p_relopexp_rel','pars.py',254),
  ('relopexp -> relopexp LE exp','relopexp',3,'p_relopexp_rel','pars.py',255),
  ('relopexp -> relopexp GE exp','relopexp',3,'p_relopexp_rel','pars.py',256),
  ('exp -> exp AND exp','exp',3,'p_exp_and','pars.py',261),
  ('exp -> exp OR exp','exp',3,'p_exp_or','pars.py',265),
  ('exp -> NOT exp','exp',2,'p_exp_not','pars.py',269),
  ('const -> TRUE','const',1,'p_const','pars.py',274),
  ('const -> FALSE','const',1,'p_const','pars.py',275),
  ('exp -> ID LRB explist RRB','exp',4,'p_exp_fun','pars.py',283),
  ('exp -> ID LRB RRB','exp',3,'p_exp_fun','pars.py',284),
  ('dec -> funcdec','dec',1,'p_dec_funcdec','pars.py',290),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB COLON type block','funcdec',8,'p_funcdec','pars.py',295),
  ('funcdec -> FUNCTION ID LRB paramdecs RRB block','funcdec',6,'p_funcdec','pars.py',296),
  ('paramdecs -> paramdecslist','paramdecs',1,'p_paramdecs','pars.py',305),
  ('paramdecs -> <empty>','paramdecs',0,'p_paramdecs','pars.py',306),
  ('paramdecslist -> paramdec','paramdecslist',1,'p_paramdecslist','pars.py',315),
  ('paramdecslist -> paramdecslist COMMA paramdec','paramdecslist',3,'p_paramdecslist','pars.py',316),
  ('paramdec -> ID COLON type','paramdec',3,'p_paramdec','pars.py',325),
  ('paramdec -> ID LSB RSB COLON type','paramdec',5,'p_paramdec','pars.py',326),
  ('stmt -> RETURN exp SEMICOLON','stmt',3,'p_stmt','pars.py',335),
]

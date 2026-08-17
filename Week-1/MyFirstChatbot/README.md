### Key Variables
- `model` = "llama2" (or mistral)
- `history` = list of {user, assistant} dicts
- `context_limit` = 5 (keep last 5 messages)
- `system_prompt` = "You are a helpful assistant."

### Error Cases to Handle
1. Ollama server not running
2. Model not installed
3. Invalid JSON file
4. Empty input
5. Keyboard interrupt (Ctrl+C)

## Implementation Steps

### Saturday (8-10 AM): Core
- [ ] Basic chat loop (input → model → output)
- [ ] JSON save/load
- [ ] Test with restart

### Saturday (3-7 PM): Add Features
- [ ] Context management (last 5 messages)
- [ ] Error handling
- [ ] Clean code

### Sunday (8-10 AM): Polish
- [ ] Fix bugs
- [ ] Test edge cases
- [ ] Code cleanup

### Sunday (3-7 PM): Ship
- [ ] Write README
- [ ] Create requirements.txt
- [ ] Git commit & push

----------------------------------------------------------

User Input
↓
Load History (chat_history.json)
↓
Build Context (last 5 messages + system prompt)
↓
Call Ollama (ollama.generate)
↓
Print Response
↓
Save to History
↓
Repeat
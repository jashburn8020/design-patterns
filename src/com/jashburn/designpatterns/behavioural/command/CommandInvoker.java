package com.jashburn.designpatterns.behavioural.command;

import java.util.Deque;
import java.util.LinkedList;

class CommandInvoker {

	private Deque<Command> invokedCommands;

	CommandInvoker() {
		this.invokedCommands = new LinkedList<>();
	}

	void invokeCommand(Command command) {
		command.execute();
		invokedCommands.addFirst(command);
	}

	void undoCommands() {
		while (invokedCommands.size() > 0) {
			invokedCommands.removeFirst().undo();
		}
	}
}

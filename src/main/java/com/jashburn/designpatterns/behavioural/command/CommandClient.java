package com.jashburn.designpatterns.behavioural.command;

public class CommandClient {

	void executeCommands(CommandInvoker invoker) {
		Receiver receiver = new StorageReceiver();
		Command storeWidgetMetadataCmd = new StoreWidgetMetadataCommand(receiver, "some metadata");
		Command storeWidgetCmd = new StoreWidgetCommand(receiver, new Widget() {/* empty */});

		invoker.invokeCommand(storeWidgetMetadataCmd);
		invoker.invokeCommand(storeWidgetCmd);
	}

	void undoCommands(CommandInvoker invoker) {
		invoker.undoCommands();
	}

	public static void main(String[] args) {
		CommandClient client = new CommandClient();
		CommandInvoker invoker = new CommandInvoker();

		client.executeCommands(invoker);
		client.undoCommands(invoker);
	}

}

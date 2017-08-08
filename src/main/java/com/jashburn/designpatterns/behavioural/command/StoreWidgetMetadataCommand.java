package com.jashburn.designpatterns.behavioural.command;

class StoreWidgetMetadataCommand implements Command {

	private Receiver receiver;
	private String metadata;
	private long metadataId;
	private boolean executed;

	StoreWidgetMetadataCommand(Receiver receiver, String metadata) {
		this.receiver = receiver;
		this.metadata = metadata;
	}

	@Override
	public void execute() {
		if (!executed) {
			metadataId = receiver.storeMetadata(metadata);
			executed = true;
		}
	}

	@Override
	public void undo() {
		if (executed) {
			receiver.deleteMetadata(metadataId);
			executed = false;
		}
	}
}

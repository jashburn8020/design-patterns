package com.jashburn.designpatterns.behavioural.command;

public class StoreWidgetCommand implements Command {

	private Receiver receiver;
	private Widget widget;
	private long widgetId;
	private boolean executed;

	StoreWidgetCommand(Receiver receiver, Widget widget) {
		this.receiver = receiver;
		this.widget = widget;
	}

	@Override
	public void execute() {
		if (!executed) {
			widgetId = receiver.storeWidget(widget);
			executed = true;
		}
	}

	@Override
	public void undo() {
		if (executed) {
			receiver.deleteWidget(widgetId);
			executed = false;
		}
	}
}

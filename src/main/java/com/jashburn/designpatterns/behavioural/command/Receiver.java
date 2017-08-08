package com.jashburn.designpatterns.behavioural.command;

interface Receiver {

	long storeMetadata(String metadata);

	void deleteMetadata(long metadataId);

	long storeWidget(Widget widget);

	void deleteWidget(long widgetId);
}

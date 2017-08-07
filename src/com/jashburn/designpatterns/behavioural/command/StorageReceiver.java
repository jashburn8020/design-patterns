package com.jashburn.designpatterns.behavioural.command;

import java.util.Random;

class StorageReceiver implements Receiver {

	Random random;

	StorageReceiver() {
		random = new Random(System.currentTimeMillis());
	}

	@Override
	public long storeMetadata(String metadata) {
		long metadataId = random.nextLong();
		System.out.println("Storing metadata " + metadataId + " [" + metadata + "]");

		return metadataId;
	}

	@Override
	public void deleteMetadata(long metadataId) {
		System.out.println("Deleting metadata " + metadataId);
	}

	@Override
	public long storeWidget(Widget widget) {
		long widgetId = random.nextLong();
		System.out.println("Storing widget " + widgetId + " [" + widget + "]");

		return widgetId;
	}

	@Override
	public void deleteWidget(long widgetId) {
		System.out.println("Deleting widget " + widgetId);
	}
}

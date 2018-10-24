# coding=utf8
__author__ = 'ls'
import sys
import codecs

reload(sys)
sys.setdefaultencoding("utf-8")


def output_result(map_app_count, output_count=-1):
	map_app_count = sorted(map_app_count.items(), key=lambda d: d[1], reverse=True)
	index = 0;
	total_count = 0;
	output_item = True;
	if output_count == -1:
		output_count = len(map_app_count)
		output_item = False;

	for app, count in map_app_count:
		if output_item:
			print(app + ' ' + str(count))
		index += 1;
		total_count += count;
		if index > output_count:
			break;
	if output_item is False:
		print('total count = ' + str(total_count))


def statistics(file, min_count, stat_count=-1):
	playing_app_count = {};
	other_app_count = {};
	all_count = 0;
	ignore_count = 0;
	invalid_count = 0;
	multi_count = 0;  # 有些人 被统计多个应用
	for line in file:
		all_count += 1;
		vec = line.split('\t')

		# print(len(vec))
		if len(vec) >= 5:
			is_playing = int(vec[4])
			apps = vec[3].split('#');

			app_count = other_app_count;
			if is_playing == 1:
				app_count = playing_app_count;

			tar = {}
			for app in apps:
				count = 1
				if app in tar:
					count = tar[app] + 1;
				tar[app] = count;

			multi_count += len(tar)
			ignore = True;
			for app in tar:
				if tar[app] > min_count:
					count = 1
					if app in app_count:
						count = app_count[app] + 1;
					app_count[app] = count;
					ignore = False;
				# else:
				#	print(app + ' ' + str(tar[app]))
			if ignore:
				ignore_count += 1;
		else:
			invalid_count += 1;

	print('all count = ' + str(all_count) + ' ignore count = ' + str(ignore_count) + ' invalid_count = ' + str(
		invalid_count) + ' multi_count = ' + str(multi_count))
	print ('playing music ')
	output_result(playing_app_count, stat_count);

	# playing_app_count = sorted(playing_app_count.items(), key=lambda d: d[1],reverse=True)
	# print playing_app_count;
	# for r in playing_app_count:
	#	print(r + ' ' + str(playing_app_count[r]))

	print('no playing music')
	output_result(other_app_count, stat_count);


# other_app_count = sorted(other_app_count.items(), key=lambda d: d[1],reverse=True)
# print(other_app_count)
# for r in other_app_count:
#	print( r + ' ' + str(other_app_count[r]))

if __name__ == "__main__":
	statistics(sys.stdin.name());
# statistics(sys.stdin,2,1000)
# file_name = r'f:\0726_16.txt';
# file_name = r'f:\stat\0729.txt';

# statistics(codecs.open(file_name),2,1000)
